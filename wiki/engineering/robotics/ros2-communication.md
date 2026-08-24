---
tags: [wiki, modules, robotics]
last_updated: "2026-08-17"
---

# ROS2 Communication — DDS/RTPS Internals · QoS · Discovery · Security

> The protocol layer: what RTPS actually sends, how discovery works at the packet level, every QoS policy and its dependency chain, the domain ID port math, and SROS2 security.
> **Sources:** design.ros2.org (ROS on DDS, QoS), OMG DDS/RTPS specs, docs.ros.org (About-Domain-ID, QoS, Middleware Vendors), eProsima/Vulcanexus docs, arXiv 2509.03381 (QoS dependency analysis), iotdigitaltwinplm 2026 (DDS vs Zenoh).
> **Related:** [[engineering/robotics/index|Robotics & ROS2 Hub]] · [[ros2-architecture]] · [[ros2-tools-debugging]] · [[modules/index|Modules Catalog]] · [[wiki/index|Wiki Home]]

## 1. RTPS — the wire protocol under the hood

DDS vendors implement **RTPS** (Real-Time Publish-Subscribe): a peer-to-peer protocol over UDP (also TCP/SHM). The actors:

```
DataWriter ──[RTPS messages]──▶ DataReader
   │                                │
   └─ Heartbeat ────────────────────┘
      (sequence number, high-water mark)
   ── data(seq=1..N) ───────────────▶
   ◀── AckNack(missing seqs) ────────   (reliable mode)
   ── resend missing ───────────────▶
```

- **DataWriter**: sequence-numbers every sample.
- **Heartbeat**: "I have data up to seq N."
- **AckNack**: reader reports gaps; writer retransmits → this is *what `reliable` means at the packet level*.
- **Best effort**: writer fires samples with no handshake — data can be dropped (fine for sensor streams, catastrophic for commands).

## 2. Discovery — how nodes find each other (no master)

DDS discovery is **distributed** and has two phases:

| Phase | Protocol | What happens |
|---|---|---|
| Participant discovery | **SPDP** (multicast) | Every participant announces itself; a `hello`/`acknowledgment` exchange |
| Endpoint discovery | **SEDP** (reliable) | Participants exchange their Writers/Readers with topic names + QoS |

```
   Node A                          Node B
     │── SPDP multicast ──▶         │
     │◀── SPDP response ───         │
     │── SEDP: "I write /scan" ──▶  │
     │◀── SEDP: "I read /scan" ──── │
     │── data now flows (RTPS) ──▶  │
```

### Scaling & when discovery breaks

- **Simple discovery** works on one LAN (multicast). Failures: multicast blocked by firewall/VLAN, wrong `ROS_DOMAIN_ID`, different RMW, or **node count**: >~119 participants on one host exhaust a domain's multicast port allocation → new nodes go "deaf". Raise with vendor XML (`mutation_tries`) or move to a discovery server.
- **Discovery Server** (Fast DDS/Cyclone): central rendezvous — nodes connect to the server (TCP, no multicast). Standard for **fleets, WAN, firewalled deploys**. Same for **Zenoh router** (`zenohd`) in the Zenoh RMW.
- Multi-robot isolation: separate `ROS_DOMAIN_ID` per robot is the simplest correct answer.

## 3. The ROS_DOMAIN_ID — port math

The domain ID selects a UDP port range via the DDS spec:

```
base = 7400 + 250 × domain_id            (fixed per domain)
participant traffic: base + 10..15       (multicast + unicast)
builtin writers/readers: base + 0..9     (discovery)
user data writers/readers: base + 16..119 (derived: PB + D0*i + D1*i*j ...)
```

- Range **0–232**. Different domains literally use different sockets → hard isolation at the network layer.
- Resource limits (the 119/domain count) come from this allocation; huge fleets → discovery server or vendor tuning.

## 4. QoS — the complete policy set and its dependency chain

DDS defines **20+ policies**; ROS2 exposes the 9 that matter. Publisher and subscriber only match if compatible — **mismatch = silent no-connect**.

### 4.1 The policies

| Policy | Options | Meaning | Per-entity |
|---|---|---|---|
| **Reliability** | reliable / best_effort | reliable = retransmit (heartbeat/AckNack); best_effort = fire-and-forget | pub & sub |
| **Durability** | volatile / transient_local | Do late joiners get history? (transient_local replays from writer cache) | pub & sub |
| **History** | keep_last / keep_all | Cache size policy | pub & sub |
| **Depth** | int | Cache size for keep_last | pub & sub |
| **Deadline** | duration | Max gap between samples — a *liveness guarantee* that can be violated (→ detector fires) | pub & sub |
| **Liveliness** | automatic / manual | Node-alive signals; dead participant → you detect it | pub & sub |
| **Lifespan** | duration | Samples expire after T (drop stale data) | pub only |
| **Ownership** | exclusive / shared | Exclusive: only strongest writer's samples used (leader election) | pub & sub |
| **Partition** | string | Logical groups (ROS2 default: "no partition" = global) | pub & sub |

### 4.2 The compatibility matrix (memorize the failure mode)

| Publisher | Subscriber | Result |
|---|---|---|
| reliable | reliable | ✅ match |
| reliable | best_effort | ✅ match (subscriber accepts whatever arrives) |
| best_effort | best_effort | ✅ match |
| **best_effort** | **reliable** | ❌ **no match** — the classic bug |
| transient_local | volatile | ✅ match, but late joiners get nothing |
| transient_local | transient_local | ✅ late joiners replay history |
| different partition | | ❌ isolated |
| deadline/liveliness mismatched | | match, but liveness checks are weaker side |

**Why sensors are best_effort:** for images at 30 Hz, retransmitting a dropped frame adds latency that is worse than losing it. ROS2's built-in profiles encode this:

| Profile | Reliability | Durability | Depth | When |
|---|---|---|---|---|
| default | reliable | volatile | 10 | general |
| sensor_data | best_effort | volatile | 5 | camera/LiDAR |
| services_default | reliable | volatile | 10 | services |
| parameters | reliable | volatile | 1000 | parameter service |

### 4.3 The dependency chain (why "reliable + depth too small" drops data)

arXiv 2509.03381 maps inter-policy dependencies:

```
RELIABLE ──requires──▶ HISTORY depth large enough for the retransmission window
   └── requires ──▶ RESOURCE_LIMITS (max samples) for keep_all
   └── requires ──▶ LIFESPAN ≥ RTT  (if samples expire before retransmit → reliable
                                     silently degrades to best_effort!)
DURABILITY(transient_local) ──requires──▶ RELIABLE  (must be able to resend history)
   └── requires ──▶ HISTORY depth ≥ (RTT/publish_period) + 2
DEADLINE ──constrains──▶ LIFESPAN, HISTORY
```

Practical rules:
- `reliable` + tiny depth → write() blocks / samples dropped under load.
- `lifespan` shorter than round-trip time → reliable behavior silently lost.
- `transient_local` + non-reliable writer is **invalid** in major implementations.
- Set `depth` to a few × worst-case burst (a common "spawned many nodes, only some connected" bug is fixed by depth>1).

## 5. Middleware vendors & transport

| RMW | Notes | When |
|---|---|---|
| **Fast DDS** (default) | Most features, biggest user base, discovery-server tooling | default |
| **Cyclone DDS** | Often lower latency; simple config | latency-sensitive LAN |
| **rmw_zenoh** | Zenoh protocol, not wire-compatible with DDS; single JSON5 router config; WAN/robot-cloud native | fleets over WAN, cloud robots |
| Connext / GurumDDS | commercial support, cert paths | industrial |

**Shared memory:** intra-process (components, §6 of architecture page) and Iceoryx offer zero-copy paths for the tightest loops. Same-host UDP is bypassed → big latency win for image pipelines.

## 6. Security — SROS2

- **DDS Security** (built-in in vendors): per-participant **X.509 certificates + governance files** (which topics, which permission), signed and encrypted discovery/data.
- `sros2` tooling generates keys/CA for your fleet.
- Cost: PKI setup, per-node cert management; the *mechanism* (identity + permission + crypto on the wire) is mature — this is how ROS2 is deployed in regulated systems.

## 7. Debugging communication — the complete procedure

```
1. Environment consistency (everywhere):
     echo $ROS_DOMAIN_ID   |  echo $RMW_IMPLEMENTATION   |  source /opt/ros/jazzy/setup.bash
2. Discovery works?    ros2 node list   (same results on both machines?)
3. Topic alive?        ros2 topic list ; ros2 topic info /scan -v   ← QoS of BOTH sides
4. Data flowing?       ros2 topic hz /scan ; ros2 topic echo /scan --once
5. Network level:      multicast enabled? tcpdump -i any udp port 7400 (domain 0)
6. Fleet/WAN scale:    move to discovery server / Zenoh router
7. Security on?        certs & governance loaded on both sides
```

## 8. Latency/jitter you should actually measure

```
pub → rmw serialize → DDS write → transport → DDS read → rmw deserialize → callback
```

Measure the **end-to-end** number (tracing, §tools page) not just one hop. At scale, queue depths, QoS profile, executor choice, and host tuning dominate over the network itself.

Next: **[[ros2-installation-setup]]** — building and structuring ROS2 systems.
