---
tags: [wiki, modules, robotics]
last_updated: "2026-08-17"
---

# ROS2 Tools & Debugging — Introspection · Tracing · Performance · Failure Analysis

> Engineering-grade debugging: the `ros2` CLI surface, live visualization, recording/replay, **tracing-based latency analysis** (ros2_tracing/CARET/LTTng), threading & real-time pitfalls, and the systematic methodology used on autonomous-vehicle stacks.
> **Sources:** docs.ros.org (CLI, tf2, rosbag, ros2_tracing), Autoware_Perf (JSA/Elsevier 2022), CARET docs, Polymath Robotics executor post, Robotisim Nav2 guide.
> **Related:** [[01-Areas/Engineering/robotics/index|Robotics & ROS2 Hub]] · [[ros2-communication]] · [[ros2-architecture]] · [[wiki/index|Modules Catalog]] · [[wiki/index|Wiki Home]]

## 1. The full `ros2` CLI surface

| Command | What it tells you / does |
|---|---|
| `ros2 node list` · `ros2 node info <n>` | who's alive; the node's entities |
| `ros2 topic list [-t]` · `ros2 topic info <t> -v` | topics + types + **QoS of both sides** |
| `ros2 topic echo/hz/bw/delay` | content, rate, bandwidth, **latency per message** |
| `ros2 service list [-t]` · `ros2 service call <s> <type> {...}` | services + manual invocation |
| `ros2 action list` · `ros2 action send_goal <a> <type> {...} --feedback` | actions + goals |
| `ros2 param list/get/set/dump` | tuning, snapshot to YAML |
| `ros2 interface list/show/proto` | interface definitions |
| `ros2 pkg list` · `ros2 pkg prefix <pkg>` | installed packages, their install prefix |
| `ros2 launch <pkg> <file>` | run launch files |
| `ros2 lifecycle list/get/set` | lifecycle node state control |
| `ros2 multicast` / `ros2 doctor` | network/discovery health |
| `ros2 daemon stop/start` | restart the graph cache daemon |
| `ros2 bag record/play/info` | recording & replay |

## 2. Visualization & introspection GUIs

| Tool | Strength | When |
|---|---|---|
| **RViz2** | robot model, TF tree, scans, maps, costmaps, paths | the default 3D view |
| **rqt_graph** | live topic graph | "who talks to whom" at a glance |
| **rqt_console** | cross-node logs | warnings/errors aggregation |
| **rqt_tf_tree** | frame tree GUI | TF debugging |
| **PlotJuggler** | time-series of any topic | PID tuning, `/odom` sanity |
| **Foxglove Studio** | modern all-in-one | bags, 3D, plots, performance |

## 3. Recording & replay — rosbag2 deep

```bash
ros2 bag record /scan /odom /cmd_vel -o run1          # select topics
ros2 bag record -a -o run1                            # everything
ros2 bag play run1 --clock                            # + /clock → use_sim_time:=true
ros2 bag info run1                                    # duration, topics, types, size
ros2 bag convert ...                                  # storage plugin conversion
```

Engineering uses:
- **Repro**: record a failing behavior once, replay it forever while you fix code (time-travel debugging).
- **Determinism**: same bag + same code = same inputs; the *only* way to debug nondeterministic bugs.
- **Simulation of sensors**: feed recorded `/scan` to your stack to test perception offline.
- Compression & plugins: SQLite3 (default) / MCAP storage; `zstd` compression for large runs.

## 4. Latency & performance analysis — tracing (the professional layer)

Latency = time from **sensor sample → perception → planning → command** (end-to-end). Log timestamps alone can't attribute jitter; **tracing** can.

```
ros2_tracing (LTTng kernel+user events)
   └─ tracepoints: callback_start/end, publish, subscription, executors, rmw, DDS
        └─ tools: tracetools_analysis, CARET (chain-aware evaluation)
             └─ output: per-callback duration, communication latency, chain latencies,
                        CPU/IRQ overhead, priority inversion evidence
```

Workflow (used by Autoware/CARET):

```bash
export ROS_TRACE_DIR=$HOME/ros_traces
ros2 trace start                                    # start LTTng session
# ... run your system / play a bag ...
ros2 trace stop                                     # session closed
caret analyze ...                                   # or tracetools_analysis scripts
```

**What you learn** (this is the difference between "it's slow" and "I know why"):

| Metric | Meaning |
|---|---|
| Callback execution time | how long YOUR code runs |
| Callback start latency | scheduling delay — executor/thread contention |
| Publish→subscribe latency | middleware + transport cost |
| End-to-end chain latency | sensor→actuator total (the number that matters) |
| CPU/IRQ interference | OS-level jitter sources |

This is how you *prove* the fix (executor swap, callback group split, QoS change) moved the number.

## 5. Threading & real-time failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Callbacks starve randomly | all work in ONE mutually-exclusive group | split callback groups |
| One slow node blocks others | single-threaded executor | multi-threaded / separate groups |
| Latency spikes under load | wait-set polling overhead, thread contention | Events/CBG executor (Lyrical+) or WaitSet |
| Priority inversion | executor has no priorities | explicit WaitSet / rclc (LET), PREEMPT_RT |
| Busy-wait (100% CPU, nothing ready) | multithreaded executor wait-set churn | check starvation fixes / newer executor |

Real-time checklist: PREEMPT_RT kernel, no CPU frequency scaling, pin threads (taskset/`isolcpus`), lock memory, deterministic allocators, message depths sized not unbounded, tracing enabled in CI.

## 6. Network / DDS debugging

```bash
ros2 multicast receive                      # is multicast working?
ip addr show                                # interface UP? VLANs?
tcpdump -i any udp and port 7400            # see SPDP discovery traffic (domain 0)
ros2 doctor                                 # environment + discovery report
export ROS_LOCALHOST_ONLY=1                 # isolate to this machine (dev)
```

Scale-related: >~119 participants per host → discovery server or vendor `mutation_tries` tuning (see [[ros2-communication]] §2).

## 7. Nav2 debugging — the evidence pipeline

Debug **one `NavigateToPose` goal**; find where evidence stops:

| Stage | Check | If broken |
|---|---|---|
| Goal accepted | `/navigate_to_pose` action info | lifecycle active? goal in map? |
| Map loaded | `/map` publishing, RViz world | map_server, YAML path, `use_sim_time` |
| Localized | `/amcl_pose` stable, `map→odom` | initial pose, scan frame, AMCL params |
| Global path | `/plan` in RViz | global costmap, planner plugin, goal blocked |
| Local motion | `/cmd_vel` publishing | local costmap, DWA/TEB/MPPI, footprint |
| Robot moves | `/odom` changes | ros2_control/driver, cmd_vel accepted |

**Symptom → cause table:**

| Symptom | Most likely cause |
|---|---|
| Robot spins forever | wrong heading / recovery loop |
| Path through walls | static layer/costmap mismatch with map |
| Goal rejected | outside map / in obstacle / Nav2 inactive |
| Costmap full of obstacles | wrong sensor frame, footprint, inflation |
| "No transform available" | broken TF, frame typo, sim-time mismatch |
| Path lags behind robot | planner/controller rate or costmap update too slow |

## 8. The systematic debug loop (use in this order)

```
0. REPRODUCE: bag record the failing run (never debug a live only)
1. ros2 doctor                     → environment/discovery
2. ros2 node list / topic list     → is it connected?
3. ros2 topic info <t> -v          → QoS mismatch?
4. ros2 topic echo/hz <t>          → is data flowing, at what rate?
5. rqt_graph / rqt_console         → wiring + logs
6. view_frames / tf2_echo          → frame correctness
7. bag play --clock                → deterministic repro
8. tracing (ros2_tracing/CARET)    → latency attribution
9. change ONE variable             → re-measure (before/after numbers)
```

## 9. Gotchas cheat (engineering additions)

| Gotcha | Fix |
|---|---|
| `ros2 node list` stale | `ros2 daemon stop && ros2 daemon start` |
| Python edits don't apply | `--symlink-install` + re-source |
| Works on PC, not robot | `ROS_DOMAIN_ID`/`RMW_IMPLEMENTATION` mismatch |
| Sim time bugs | `use_sim_time` consistent everywhere |
| Gazebo vs RViz disagree | physics vs model — check inertials (Gazebo) vs TF (RViz) |
| Deterministic-slow vs jitter | jitter = scheduling/OS → tracing; constant = algorithm |
| Depth=1 connections fail | QoS depth too small for bursty pub |

Next: **[[ros2-cheatsheet]]** — the full command + code reference.
