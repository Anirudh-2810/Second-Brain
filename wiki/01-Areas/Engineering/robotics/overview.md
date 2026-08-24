---
tags: [wiki, modules, robotics]
last_updated: "2026-08-17"
---

# Robotics — Overview & Mental Model

> Robotics = **embodied, real-time intelligence**: a dynamical system that senses a noisy world, estimates its state, decides under constraints, and actuates within hard timing budgets — every few milliseconds, forever.
> **Sources:** Spong et al. (*Robot Modeling and Control*), Thrun et al. (*Probabilistic Robotics*), LaValle (*Planning Algorithms*), ROS2 docs, industry overviews (market ~$200B+ by 2030).
> **Related:** [[01-Areas/Engineering/robotics/index|Robotics & ROS2 Hub]] · [[robotics-fundamentals]] · [[wiki/index|Modules Catalog]] · [[wiki/index|Wiki Home]]

## 1. Definition — the loop as a control system

A robot is a **closed-loop dynamical system**: a state `x` evolves under control `u`, perturbed by disturbances, observed through noisy sensors.

```
ẋ = f(x, u, w)        dynamics + disturbances
y = h(x) + v           noisy measurement model

                    ┌──────────────────────────────┐
  setpoint ──(+)──▶ │  planner + controller (C)    │── u ──▶ [Robot P] ──▶ state x
              ▲     └──────────────────────────────┘            │
              │                                                 ▼
              └─────────────── estimator (KF/EKF/particle) ◀── sensors y
```

This *single picture* contains the whole field:

| Block | Question | Tools |
|---|---|---|
| **P** (plant) | How does the world move it? | kinematics/dynamics, simulators |
| **Sensors y** | What do we observe? | LiDAR, camera, IMU, encoders |
| **Estimator** | What's our belief of x? | KF, EKF, UKF, particle filter |
| **C** (control) | What do we command? | PID, LQR, MPC |
| **Setpoint** | What *should* happen? | planning (A*, RRT, DWA), mission logic |

**The single most important habit in robotics:** for any behavior, name its *state, control, sensors, and timing*. If you can't, you can't build it.

## 2. The real-time dimension (what makes it *engineering*)

Software robotics is bounded by **deadlines and budgets**:

| Loop | Typical rate | Deadline budget | Examples |
|---|---|---|---|
| Inner motor loop | 100 Hz – 1 kHz | 1–10 ms | motor velocity PID (ros2_control) |
| Control/localization | 50–200 Hz | 5–20 ms | odometry, local planner, EKF |
| Perception | 10–60 Hz | 16–100 ms | camera, object detection |
| Navigation | 1–20 Hz | 50 ms – 1 s | global planner, SLAM loop closures |
| Mission | 0.1–1 Hz | seconds | task scheduling, behavior trees |

**End-to-end latency** (sensor → compute → command) is the number that matters — e.g., for a car at 25 m/s, 200 ms of latency = 5 m of travel. This is why:
- **Real-time considerations** exist at all (PREEMPT_RT kernels, executor determinism).
- **Tracing/measurement** tools (ros2_tracing, CARET) are first-class, not nice-to-have.
- **Simulation + replay (rosbag)** are mandatory: you cannot tune safety-critical loops live.

## 3. The software stack (with real ROS2 layers)

```
┌────────────────────────────────────────────────────────────┐
│  Mission / behavior .......... behavior trees, state machines │
├────────────────────────────────────────────────────────────┤
│  Autonomy ................... Nav2 (SLAM/planner/control)     │
│                             MoveIt (manipulation)            │
├────────────────────────────────────────────────────────────┤
│  Middleware ................. rclcpp / rclpy / rcl → rmw       │
│                             (topics/services/actions/params) │
├────────────────────────────────────────────────────────────┤
│  OS ......................... Ubuntu + PREEMPT_RT (optional)  │
├────────────────────────────────────────────────────────────┤
│  Hardware abstraction ....... ros2_control (drivers, RT)      │
├────────────────────────────────────────────────────────────┤
│  Hardware ................... actuators + sensors + compute   │
└────────────────────────────────────────────────────────────┘
```

**Every layer is a filter that adds latency and a place where failure hides.** The middleware layer (ROS2) is what this module is built around — see [[ros2-architecture]].

## 4. The trade-off triangle

```
              Performance (speed, precision)
                    /\
                   /  \
                  /    \
         Cost ────────── Robustness (safety, reliability)
```

Every robotics decision is a point in this triangle:
- **Sensors**: cheap LiDAR (short range, low res) vs solid-state 3D (expensive) — localization *quality* is bounded by sensor noise (`R` in the KF).
- **Compute**: onboard Jetson (limited) vs server (low latency impossible) → perception/model size trades.
- **Algorithms**: PID (cheap, linear) vs MPC (expensive, constrained) — the winner depends on the *speed × nonlinearity × safety* of the task.

## 5. Types of robots & their physics

| Class | Dominant dynamics | Core problems |
|---|---|---|
| Mobile wheeled (differential) | planar, nonholonomic | odometry drift, SLAM, local planning |
| Manipulator arms | rigid-body chains | IK, singularities, force control, collision |
| Aerial (multi-rotor) | underactuated 6-DOF | attitude control, state estimation, wind |
| Legged | hybrid (contact transitions) | balance, footstep planning, ground reaction |
| Autonomous vehicle | high-speed planar + prediction | perception, prediction, decision, safety |
| Underwater/space | nonlinear/harsh | odometry (no GPS), robustness |

## 6. Where this module connects to the vault

| Vault topic | Robotics connection | Specific link |
|---|---|---|
| AI/ML | perception (CNN), RL control (PPO), planning | [[01-Areas/AI-Data/ai/index|AI Hub]] |
| Mathematics | transforms (LinAlg), Bayes (prob), dynamics (ODE) | [[01-Areas/Engineering/mathematics/overview|Mathematics]] |
| Programming/CS50 | every node is a program; data structures for grids/trees | [[programming/cs50/index|CS50]] |
| OOP | node/interface/package architecture | [[programming/object-oriented-programming/overview|OOP]] |
| C++ systems | real-time loops, deterministic memory | [[01-Areas/AI-Data/ai-ml/matching-engine-cpp|Matching Engine]] |
| Self-Mastery | running multi-week engineering builds | [[01-Areas/Self-Dev/self-mastery/overview|Self-Mastery]] |
| Quant/backtesting | *same* discipline: data → model → decision loop, look-ahead bugs | [[01-Areas/AI-Data/ai-ml/event-driven-backtesting|Backtesting]] |

## 7. Key takeaways

1. Robotics = **estimation + control + planning on a real-time dynamical system**. Name state/control/sensors/timing before coding.
2. **Latency budget** is the master constraint — it decides executor choice, language (C++ vs Python), and even algorithm.
3. ROS2 is the **middleware** that glues the blocks; it doesn't remove the math, it *distributes* it into nodes.
4. Simulation + bag replay are **engineering tools**, not toys — they make the system testable.
5. Everything in this vault's robotics pages is one block in the diagram above.

Next: **[[robotics-fundamentals]]** — the derivations (kinematics → dynamics → control → estimation → SLAM → planning → perception), or **[[ros2-architecture]]** for the software.
