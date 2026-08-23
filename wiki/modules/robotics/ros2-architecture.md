---
tags: [wiki, modules, robotics]
last_updated: "2026-08-17"
---

# ROS2 Architecture — Layers · Nodes · Executors · Time · Real-Time

> The internal architecture: from the DDS wire up to your Python callback. Understand the **layered design**, how **executors** actually schedule callbacks, and why **time** is its own problem.
> **Sources:** docs.ros.org (Concepts, About-Executors, Using-callback-groups), design.ros2.org, Casini et al. (ECRTS 2019 executor analysis), Polymath Robotics — "Execution Management in rclcpp" (Lyrical executor benchmarks), ros2_tracing/Autoware_Perf literature.
> **Related:** [[modules/robotics/index|Robotics & ROS2 Hub]] · [[ros2-communication]] · [[ros2-installation-setup]] · [[modules/index|Modules Catalog]] · [[wiki/index|Wiki Home]]

## 1. The layered architecture (memorize this stack)

```
┌─────────────────────────────────────────────────────────────┐
│  Application (your nodes)          rclcpp (C++) / rclpy      │
├─────────────────────────────────────────────────────────────┤
│  Client library (rcl)              common C API, types, time │
├─────────────────────────────────────────────────────────────┤
│  Middleware wrapper (rmw)          RMW interface abstraction │
├─────────────────────────────────────────────────────────────┤
│  DDS implementation                Fast DDS / CycloneDDS ...  │
├─────────────────────────────────────────────────────────────┤
│  Transport                        UDP/TCP/Shared Memory      │
└─────────────────────────────────────────────────────────────┘
```

- **rclcpp / rclpy** — the idiomatic API you write. Share the same **rcl** C layer.
- **rcl** — language-neutral core (node, timer, time, graph). Why both languages behave identically.
- **rmw** — the "ROS Middleware Wrapper": a stable interface so any DDS vendor can plug in. Switching `RMW_IMPLEMENTATION` swaps the entire transport without touching your code.
- **DDS/RTPS** — actual discovery + data distribution (details in [[ros2-communication]]).

```
   Application A (rclpy)                Application B (rclcpp)
        │                                     │
        └── rcl (C API)                       └── rcl (C API)
              │                                     │
              └────── rmw interface ◄───────────────┘
                       │
                  Fast DDS / Cyclone / Zenoh
                       │
                    UDP / SHM / IPC
```

## 2. Nodes & entities

A **node** is a container of **entities**:

| Entity | Purpose |
|---|---|
| Publisher | Sends messages on a topic |
| Subscription | Receives messages, fires callback |
| Service server/client | Request–response |
| Action server/client | Goal + feedback + result |
| Timer | Periodic callback (a "clock event") |
| Parameter | Key–value config |
| Waitable | Custom entity the executor can wait on |

Every entity belongs to a **callback group** (default: one shared group). Node name must be **unique** in a graph (auto-suffix `_1`, `_2` on collision).

## 3. Executors — the scheduling engine (deep dive)

The **executor** owns the thread(s) that run callbacks. `spin()` loops: *collect entities → wait for ready ones → service callbacks.*

### 3.1 The classic executors

| Executor | Threads | Behavior |
|---|---|---|
| **SingleThreadedExecutor** | 1 | All callbacks serialized on one thread. Simple, deterministic-enough, but one slow callback blocks everything |
| **MultiThreadedExecutor** | N | Pool of threads; parallelism **governed by callback groups** |
| **StaticSingleThreadedExecutor** | 1 | Caches the wait-set (entity list) → far less CPU; deprecated/merged in newer distros |

### 3.2 Wait sets — how the executor polls

The executor builds a **wait set**: a flat collection of entities (subs, servers, timers, waitables), passes it to the DDS layer, and blocks until *something* is ready. Key semantics (Casini et al., ECRTS 2019):

1. The wait set reports only *whether a topic has messages*, **not how many**.
2. The executor drains ready callbacks **round-robin**, **not FIFO** per topic.
3. **Timer events get priority** over message callbacks.
4. The wait set is **rebuilt each iteration** in the classic executors → measurable CPU overhead at high entity counts.

### 3.3 Callback groups — your concurrency control

```
type MutuallyExclusiveGroup:  only ONE callback of the group runs at a time
type ReentrantGroup:          callbacks of the group may run in parallel

rules:  callbacks in DIFFERENT groups may run in parallel (multithreaded executor)
        callbacks in the SAME mutually-exclusive group never run together
```

**Engineering rules of thumb:**
- Slow + fast work in one node → separate callback groups (e.g., image processing vs `/cmd_vel`).
- State you mutate must live in a **mutually exclusive** group (or be thread-safe).
- Independent hot paths → **reentrant** groups or separate nodes.

### 3.4 Why the classic executor is not real-time (and what fixes it)

Documented problems (ECRTS 2019; rclcpp #825):

1. **Complex mixed scheduling semantics** → impossible to do formal timing analysis.
2. **Priority inversion** — a high-priority callback can wait behind a low-priority one.
3. **No control over callback order**; no per-topic triggering.
4. **Round-robin with timer priority** gives jitter.

Mitigations that exist today:
- **`rclcpp::WaitSet`** — wait directly on entities, bypass the executor → deterministic user-defined processing sequences (this is how serious RT stacks are written).
- **`rclc` Executor (micro-ROS)** — explicit callback order + **Logical Execution Time (LET)** semantics for embedded MCUs.
- **EventsExecutor / Callback-Group-Events Executor** — event-driven instead of polling; shipped as the improved path in **Lyrical Luth** (measured ~10–15% less CPU; large wins at high entity density). Multi-threaded CBG executor still pays thread-pool context-switch cost.

```
Classic (polling):
  spin ─▶ build waitset ─▶ wait ─▶ scan results ─▶ run callbacks ─▶ repeat
  (each iteration: rebuild, scan all entities, timer-priority drain)

EventsExecutor (event-driven):
  DDS callbacks push events into a queue ─▶ worker thread services queue
  (no polling; events only when data actually arrives)
```

### 3.5 Choosing an executor (decision)

```
One fast callback? ─────────────► SingleThreadedExecutor
Multiple nodes, few callbacks ──► Single/Static
Mixed-speed callbacks, same node ─► MultiThreaded + callback groups
Hard real-time / micro-ROS ─────► rclc executor / WaitSet (bypass executor)
Latency-critical, high density ──► Events/CBG executor (Lyrical+)
```

## 4. Time in ROS2 — the second design axis

| Clock | Source | When to use |
|---|---|---|
| **ROS time** (`/clock` topic) | set by `use_sim_time:=true` | Simulation, bag replay — so everything stays synchronized |
| **Steady time** | hardware monotonic | Real-time deadlines, `std::chrono`-style |
| **System time** | wall clock | Logging, timestamps for data |

Rules:
- Timestamps on sensor messages must share one clock source or transforms break (`Lookup would result in an invalid transformation`).
- `use_sim_time=true` on all nodes when replaying a bag or running Gazebo; `false` on real hardware.
- **tf2 buffers data in time** — queries like `lookupTransform(a, b, time)` need correct clock + buffer duration (default 10 s).

## 5. Lifecycle nodes — managed state machines

State machine for stateful systems (Nav2 uses this):

```
  unconfigured ──configure()──▶ inactive ──activate()──▶ active ──deactivate()──▶ inactive
        ▲                          ▲                       │
        └──destroy()──────────────┴───────────────────────┘
```

- `configure`: allocate, load params (may fail safely → return error).
- `activate`: start publishing/processing.
- Calls go through services (`/node/configure`, `/node/activate`).
- **Why it exists:** safe startup order, clean shutdown, recovery — you don't want Nav2 planning while the map isn't loaded. This is *why* freshly-launched Nav2 sits idle until activated.

## 6. Intra-process communication & components

**Composable nodes** (a.k.a. nodelets-in-ROS2): multiple nodes loaded into **one process**, communicating through **shared memory — zero copy, zero serialization**. When latency/CPU matter and nodes are tightly coupled (camera → detection → tracking in one binary), use `rclcpp_components` to compose them. Trade-off: lose fault isolation (one crash kills all).

```
Separate processes:  A ──serialize──▶ DDS ──deserialize──▶ B      (copies, overhead)
Same process:        A ──── pointer handoff in shared memory ────▶ B  (zero-copy)
```

## 7. Message types & serialization

`.msg/.srv/.action` files → **rosidl** generates C/C++/Python classes at build time. The wire format is RTPS/CDR. Important implications:

- Field types are fixed (`float64`, `int32`, `string`, nested messages, bounded arrays) → **static memory bounds** → real-time friendly.
- Changing an interface = **ABI break** → rebuild all consumers (hence "interfaces-only package" convention).
- Inspect anything at runtime: `ros2 interface show <type>`.

## 8. ROS1 → ROS2 — what actually changed

| Aspect | ROS1 | ROS2 |
|---|---|---|
| Master/roscore | required | **none** (DDS discovery) |
| Transport | TCPROS | DDS/RTPS (UDP, SHM, Zenoh) |
| Build | catkin (CMake-only) | **colcon + ament**, multi-build-system |
| Launch | XML | **Python launch files** (full programmability) |
| Real-time | impossible | possible (PREEMPT_RT + tuning) |
| Security | none | **SROS2** (DDS PKI) |
| Single-node | node | node, component, lifecycle variants |
| API | `ros::` | `rclcpp::` / `rclpy`, `rcl` C layer |

## 9. Mental model (engineering version)

```
1. A robot = graph of NODES; nodes exchange typed messages via
   topics (streams) / services (sync) / actions (long goals) / params.
2. Behind your callback: rclpy → rcl → rmw → DDS → network, and BACK.
   That chain's total latency + jitter is your system's heartbeat.
3. The EXECUTOR is your scheduler: callback groups = your concurrency
   contract; timers win; round-robin drains; classic executors poll.
   Real-time work: WaitSet or rclc/LET, PREEMPT_RT, measure with tracing.
4. TIME is a design axis: pick one clock, set use_sim_time consistently,
   buffer tf2 queries against it.
```

Next: **[[ros2-communication]]** — what happens inside DDS (QoS, discovery, security).
