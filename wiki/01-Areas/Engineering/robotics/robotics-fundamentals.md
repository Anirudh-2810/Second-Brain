---
tags: [wiki, modules, robotics]
last_updated: "2026-08-17"
---

# Robotics Fundamentals — Kinematics · Dynamics · Control · State Estimation · SLAM · Planning · Perception

> The **engineering core** of robotics, taken to derivation level. Each section states the mathematical model, works the derivation, then maps it to the ROS2 package that implements it.
> **Sources:** Spong–Hutchinson–Vidyasagar (*Robot Modeling and Control*), Siciliano (*Robotics: Modelling, Planning and Control*), Thrun–Burgard–Fox (*Probabilistic Robotics*), LaValle (*Planning Algorithms*), Laubach et al. Nav2 concept docs, arXiv 2509.03381.
> **Related:** [[01-Areas/Engineering/robotics/index|Robotics & ROS2 Hub]] · [[overview]] · [[01-Areas/Engineering/mathematics/overview|Mathematics]] · [[wiki/index|Modules Catalog]] · [[wiki/index|Wiki Home]]

---

## 1. The Robot as a Dynamical System

A robot is a **dynamical system** — its state evolves over time under control inputs:

```
ẋ = f(x, u)          state-space dynamics (continuous)
x[k+1] = f(x[k], u[k])   discrete-time form (what software implements)
y = h(x)               measurement model (what sensors see)
```

- **State x**: pose (position + orientation), joint angles, velocities. For a mobile robot: `x = [x, y, θ, v, ω]ᵀ`.
- **Control u**: motor voltages, wheel velocity commands (`/cmd_vel`).
- **Measurement y**: LiDAR ranges, IMU, wheel counts (`/scan`, `/imu`, `/odom`).
- The whole discipline splits into four coupled problems:

| Problem | Question | Math object |
|---|---|---|
| **Kinematics** | *Where is the robot given its motion?* | transforms `T ∈ SE(3)` |
| **Dynamics** | *What forces make it move?* | ODEs `M(q)q̈ + C(q,q̇)q̇ + g(q) = τ` |
| **Estimation** | *Where am I, given noisy sensors?* | Bayes filters (KF/EKF/particle) |
| **Planning & Control** | *What do I command next?* | optimization over `x, u` |

Everything in ROS2 is one of these four, wrapped in a node.

---

## 2. Kinematics — Representing Pose

### 2.1 Rotation matrices — SO(3)

A rotation about the z-axis by angle θ:

```
      ┌ cosθ  −sinθ  0 ┐
R_z = │ sinθ   cosθ  0 │
      └  0      0     1 ┘
```

Rotation matrices are **orthogonal with det = +1**: `RᵀR = I`. Rotations compose by multiplication: rotating `v` by `R1` then `R2` is `v' = R2(R1 v) = (R2 R1) v`. **Order matters** — rotations do not commute.

### 2.2 Homogeneous transforms — SE(3)

Pose = rotation + translation, written as a 4×4 matrix:

```
      ┌ R   t ┐
T =   │ 0   1 │        R ∈ SO(3)  (3×3 rotation),  t ∈ R³ (translation)
```

A point `p` in frame B expressed in frame A: `p_A = T_AB · p_B` where `T_AB` means "the pose of B in A". Transform composition: `T_AC = T_AB · T_BC` — this is exactly what **tf2** computes for `map → odom → base_link → laser`.

Inverse transform: `T⁻¹ = [Rᵀ, −Rᵀ t; 0, 1]` (no matrix inversion needed — huge for real-time).

### 2.3 Euler angles vs quaternions

| Representation | Pros | Cons |
|---|---|---|
| Euler (roll–pitch–yaw, ZYX) | Intuitive, small | **Gimbal lock** (singularity), non-unique |
| **Quaternion** `q = (w, x, y, z)`, `‖q‖=1` | No singularity, smooth | Less intuitive, double cover (`q` = `−q`) |
| Axis-angle | Geometrically clear | Composes awkwardly |

ROS2 uses **quaternions** everywhere (`geometry_msgs/Quaternion`). Rotations compose via quaternion multiplication; apply to vector `v` as `v' = q v q*`. Conversion formulas are in `tf_transformations` / `Eigen`.

### 2.4 Denavit–Hartenberg (DH) parameters — robot arms

Every **arm** is a chain of joints; DH condenses each link's geometry into 4 numbers:

```
a_i   = distance from z_i-1 to z_i along x_i   (link length)
α_i   = rotation about x_i from z_i-1 to z_i   (link twist)
d_i   = distance from x_i-1 to x_i along z_i-1 (link offset)
θ_i   = rotation about z_i-1                  (JOINT variable, revolute)
```

The transform from link i−1 to link i is built from four elementary transforms:

```
T_i = Rot_z(θ_i) · Trans_z(d_i) · Trans_x(a_i) · Rot_x(α_i)

┌ cosθ  −sinθ·cosα   sinθ·sinα   a·cosθ ┐
│ sinθ   cosθ·cosα  −cosθ·sinα   a·sinθ │
│  0       sinα       cosα         d    │
└  0         0          0          1    ┘
```

**Forward kinematics**: `T_0n = T_1·T_2····T_n` — multiply the DH matrices. Closed-form for most arms.
**Inverse kinematics**: solve `T_0n = T_desired` for the joint vector `q`. For 6-DOF arms this decouples into a **position** subproblem (first 3 joints → wrist center) and an **orientation** subproblem (last 3 joints). Multiple solutions, singularities, and joint limits make IK the interesting problem.

### 2.5 Differential-drive mobile robot — full model

The canonical beginner robot. Wheel velocities `(v_L, v_R)` → robot velocity:

```
v = (v_R + v_L) / 2            forward speed
ω = (v_R − v_L) / L            angular rate (L = wheel base)
```

The **unicycle model** in global frame (this is the kinematic state equation):

```
ẋ = v·cos θ
ẏ = v·sin θ
θ̇ = ω
```

**Odometry (dead reckoning)** integrates this forward. Discrete update with measured wheel speeds and time step `Δt`:

```
θ[k+1] = θ[k] + ω[k]·Δt
x[k+1] = x[k] + v[k]·Δt·cos(θ[k] + ω[k]·Δt/2)
y[k+1] = y[k] + v[k]·Δt·sin(θ[k] + ω[k]·Δt/2)
```

This is the math inside every ROS2 odometry node (`/odom`). It drifts because it is **open-loop integration**: small errors accumulate. → motivates the filters in §5.

---

## 3. Dynamics — Forces & Accelerations

### 3.1 The rigid-body equation of motion

For a robot arm with joint vector `q`, the **Euler–Lagrange** formulation yields:

```
M(q) q̈ + C(q, q̇) q̇ + g(q) = τ
```

| Term | Meaning |
|---|---|
| `M(q)` | **Inertia matrix** (n×n, symmetric positive-definite) |
| `C(q,q̇)` | Coriolis & centrifugal effects |
| `g(q)` | Gravity torques |
| `τ` | Joint torques (control) |
| `q̈` | Joint accelerations |

For a mobile robot it's the same idea: `M v̇ + C(v) v = F`. The **Newton–Euler** formulation computes these terms recursively (outward pass for velocities/accelerations, inward pass for forces) — O(n) and what most simulators/real-time controllers use.

Simulators (Gazebo) numerically integrate this ODE every step; `ros2_control` hardware interfaces implement it for real motors.

### 3.2 Inertia & the inertia tensor

Each link has mass `m` and an **inertia tensor** (3×3, expressed in the link frame):

```
      ┌ Ixx  Ixy  Ixz ┐
I =   │ Ixy  Iyy  Iyz │
      └ Ixz  Iyz  Izz ┘
```

URDF requires these per link (`<inertial>`). A common bug: *zero inertia* or *wrong frame* → Gazebo robot explodes/tumbles. Moment of inertia of a solid cylinder of radius r, mass m: `I = (1/2)mr²`.

---

## 4. Control — Making the Robot Do What We Want

### 4.1 The closed loop, formally

```
            e = r − y                          ┌──────┐
r ──(+)──▶ [Controller C(s)] ──▶ [Plant P(s)] ──┤ sensors│──▶ y
     ▲                                          └──────┘
     └────────────────────────────────────────────────────
```

**Transfer function** (Laplace domain): `G(s) = Y(s)/R(s) = C(s)P(s) / (1 + C(s)P(s))`.
The **closed-loop poles** = roots of `1 + C(s)P(s) = 0`. Stability ⇔ all poles in left half-plane. Poles near origin (small real part) = slow; large imaginary part = oscillatory.

### 4.2 PID — the 99% controller

```
u(t) = Kp·e(t) + Ki·∫e(τ)dτ + Kd·ė(t)
```

**Why it works (math):** for a plant `ẋ = u`, plugging in `u = Kp e + Kd ė` gives the error dynamics `ÿ + Kd·ẏ + Kp·y = 0` — a **2nd-order system** with:
- natural frequency `ωₙ = √Kp`
- damping ratio `ζ = Kd / (2√Kp)`

So `Kp` sets speed, `Kd` sets damping (overshoot), `Ki` removes steady-state error by integrating residual error. This is *why* the tuning order is **P → D → I**: each term controls one eigenvalue property.

| Tuning rule (Ziegler–Nichols) | From ultimate gain `K_u`, period `T_u` at sustained oscillation |
|---|---|
| P: `0.5 K_u` · PI: `0.45 K_u, T_u/1.2` · PID: `0.6 K_u, T_u/2, T_u/8` |

### 4.3 LQR — optimal state feedback

For linear dynamics `ẋ = Ax + Bu`, choose `u = −K x` minimizing

```
J = ∫ (xᵀ Q x + uᵀ R u) dt
```

`K` comes from solving the **algebraic Riccati equation** `AᵀP + PA − PBR⁻¹BᵀP + Q = 0`, then `K = R⁻¹BᵀP`. `Q` penalizes state error, `R` penalizes control effort — **tuning = choosing Q, R**. LQR is the workhorse "good linear controller" under PID.

### 4.4 MPC — constrained optimization over a horizon

At each timestep, solve:

```
minimize   Σ_{k=1..N} (x_k − x_ref)ᵀQ(x_k − x_ref) + u_kᵀRu_k
subject to x_{k+1} = f(x_k, u_k)          (dynamics)
           u_min ≤ u_k ≤ u_max            (actuator limits)
           x ∈ X_safe                     (obstacles, rollover, ...)
```

Apply only the first control, shift horizon, re-solve (**receding horizon**). MPC is what autonomous cars/drones actually run — it handles **constraints** natively, which PID/LQR cannot. Cost: compute.

### 4.5 Control stacking in a real ROS2 robot

```
Velocity goals ──► [local planner: DWA/TEB] ──► v, ω ──► [PID velocity loop] ──► [motor driver] ──► wheels
      ▲                  (Nav2 controller_server)      (ros2_control)             (hardware)
      └─────────────────── odometry / velocity feedback ──────────────────────────┘
```

Two cascaded loops: **outer** (pose/velocity tracking, 10–50 Hz) and **inner** (motor current/velocity, 100 Hz–1 kHz). ROS2's `ros2_control` abstracts the inner loop behind `ControllerManager` + hardware interfaces.

---

## 5. State Estimation — From Noisy Sensors to Belief

### 5.1 The Bayes filter (everything descends from this)

```
Bel(x_t) = η · p(z_t | x_t) · ∫ p(x_t | x_{t-1}, u_{t-1}) · Bel(x_{t-1}) dx_{t-1}
             └─measurement─┘    └────────── motion model ──────────┘
```

Predict (apply motion) then correct (apply measurement). Three instantiations:

| Filter | Distribution | Robot | When |
|---|---|---|---|
| **Kalman** | Gaussian, linear | odom/GPS fusion | LTI dynamics |
| **EKF** | Gaussian, linearized | odom+IMU, EKF-SLAM | locally smooth nonlinear |
| **Particle (PF)** | samples | AMCL localization | highly nonlinear, multi-modal |

### 5.2 Kalman filter — full derivation

Linear system with process noise `w` and measurement noise `v`:

```
x_k = A x_{k-1} + B u_k + w_k ,    w ~ N(0, Q)
z_k = H x_k + v_k ,                v ~ N(0, R)
```

**Predict:**
```
x̂⁻_k = A x̂_{k-1} + B u_k
P⁻_k = A P_{k-1} Aᵀ + Q
```
**Update:**
```
K_k = P⁻_k Hᵀ (H P⁻_k Hᵀ + R)⁻¹          (Kalman gain)
x̂_k = x̂⁻_k + K_k (z_k − H x̂⁻_k)          (innovation weighted)
P_k = (I − K_k H) P⁻_k
```

**Why the gain is optimal:** `K` is derived by minimizing the trace of the posterior covariance `P_k`. `K → 0` when measurement noise `R` is huge (trust the model); `K → H⁻¹` when process noise `Q` is huge (trust the sensor). This is why KF/EKF is the standard odom+IMU fuser.

### 5.3 EKF — linearize the nonlinear case

For `x_k = f(x_{k-1}, u_k)` and `z_k = h(x_k)`, replace `A` and `H` with **Jacobians** evaluated at the current estimate:

```
A = ∂f/∂x |_{x̂},   H = ∂h/∂x |_{x̂⁻}
```

The unicycle model from §2.5 gives the Jacobians directly. Practical note: EKF's single-Gaussian assumption fails for **kidnapped/relocalization** problems → that's why Nav2 uses **AMCL** (particle filter), which can hold multiple hypotheses.

### 5.4 IMU orientation — complementary & Mahony/Madgwick

IMU gives angular rate (good short-term, drifts) + accelerometer/magnetometer (absolute gravity/north, noisy). The trick: **complementary filter in quaternion space**:

```
q = α·q_integrated(gyro) + (1−α)·q_from_accel+mag
```

Mahony and Madgwick filters are the standard implementations (optimize the quaternion gradient to align predicted and measured gravity). Published as `/imu/data`.

---

## 6. SLAM — Mapping While Localizing

### 6.1 Problem statement

Given measurements `z_{1:T}` and controls `u_{1:T}`, estimate **both** the map `m` and the trajectory `x_{1:T}`:

```
p(x_{1:T}, m | z_{1:T}, u_{1:T})
```

Chicken-and-egg: you need the map to localize, and the pose to build the map. Solutions divide into **online filters** (EKF-SLAM, FastSLAM) and **graph/optimization methods** (modern standard).

### 6.2 Occupancy grid mapping (the map itself)

Each cell holds log-odds:

```
l(cell) = log [ p(occ) / (1 − p(occ)) ]
l ← l + inverse_sensor_model(scan, pose)
p(occ) = 1 / (1 + e^{−l})
```

Cells the beam **passes through** are cleared; the **endpoint** is marked occupied. Ray traversal uses **Bresenham's line algorithm**. That's what `map_saver_cli` outputs as `.pgm`.

### 6.3 Scan matching (frontend)

Align the new LiDAR scan to the map/past scan by minimizing

```
min_{ΔT} Σ_i ‖ R(Δθ)·p_i + Δt − q_i ‖²     (ICP)
```

**ICP**: iterate — (1) associate nearest neighbors, (2) solve the least-squares transform (SVD), (3) repeat until convergence. With a good prior (odom) a few iterations suffice.

### 6.4 Graph SLAM (backend — slam_toolbox, Cartographer)

Model the trajectory as a **factor graph**: poses are nodes, constraints (odometry edges, loop-closure edges) are factors. Solve the nonlinear least-squares

```
min_{x} Σ_{(i,j)} ‖ e_{ij}(x) ‖²_{Σ_{ij}},     e_{ij} = z_{ij} ⊖ (x_i ⊖ x_j)
```

- Odometry factors keep the chain consistent.
- When the robot revisits a place, scan matching produces a **loop closure factor** — the edge that "pulls" the whole trajectory back into consistency. This is the `graph optimization` (Gauss–Newton/LM via g2o or Ceres) that suddenly fixes the map.
- Grid-based versions (Cartographer) also do **submap** matching so loop closures are found over large areas.

### 6.5 EKF-SLAM / FastSLAM

- **EKF-SLAM**: state = robot pose + all landmarks; the filter grows quadratically with landmarks (O(n²) covariance) → tiny maps only.
- **FastSLAM**: Rao–Blackwellized — each **particle** carries its own map + pose; map posteriors are computed per-particle analytically. The ancestor of the approach `slam_toolbox`/Cartographer superseded for grid maps.

---

## 7. Motion Planning

### 7.1 Configuration space (C-space)

Planning happens in the robot's **configuration space** — the space of all possible states of its joints/pose. Obstacles become C-obstacles; planning = finding a path in the free space `C_free`. For a 2D mobile robot, C-space ≈ the costmap.

### 7.2 Grid / graph search — A*

Minimize `f(n) = g(n) + h(n)` where `g` = cost from start, `h` = **admissible heuristic** (never overestimates — e.g. Euclidean distance). Admissibility guarantees **optimality**. Nav2's global planner runs A*/Dijkstra on the costmap grid, with the inflation layer as cost.

### 7.3 Sampling-based — RRT / RRT* / PRM

For high-DOF (arms), grids explode. **RRT**:

```
T ← start
repeat:
  x_rand ← random sample in C_free
  x_near ← nearest node in T
  x_new ← step from x_near toward x_rand (steer())
  if collision_free(x_near, x_new):
      T ← T ∪ {x_new}
until x_new ≈ goal
```

Probabilistically complete (will find a path eventually), but not optimal. **RRT\*** adds rewiring (when a new node finds a cheaper connection, rewire the tree) → asymptotic optimality. **PRM**: build a roadmap graph offline, then A*/Dijkstra on it — good for repeated planning in a static map.

### 7.4 Local planning — DWA (the math of "driving to the goal safely")

At each step, sample velocity pairs `(v, ω)` in the **dynamic window** (velocities reachable this step given acceleration limits). Score each against an objective:

```
score = α·heading(v,ω) + β·clearance(v,ω) + γ·velocity(v,ω)
```

- `heading` — alignment with the goal direction
- `clearance` — distance to nearest obstacle along the arc (from the costmap)
- `velocity` — how fast it's going (avoid robot sitting still)

Pick argmax. **TEB** instead formulates the local problem as a sparse optimization (`min E(path)`) producing smooth, obstacle-aware, kinematically feasible trajectories.

### 7.5 Trajectory generation

Planned *paths* become *trajectories* (path + time) by fitting splines through waypoints. Polynomial / B-spline fits guarantee `C²` continuity (no acceleration jumps → no wheel slip / jerky motion). Nav2 controller plugins consume these as velocity commands.

---

## 8. Perception — Seeing the World

### 8.1 The pinhole camera model

A 3D point `P = (X, Y, Z)` in camera frame projects to pixel `(u, v)`:

```
┌ u ┐   ┌ fx  0  cx ┐ ┌ X/Z ┐
│ v │ = │  0  fy cy │ │ Y/Z │
└ 1 ┘   └  0   0  1 ┘ └  1  ┘
```

- `fx, fy` — focal lengths in pixels, `cx, cy` — principal point → the **intrinsics matrix K** (from camera calibration, stored in `camera_info`).
- **Extrinsics**: camera-to-robot pose (a tf2 frame). Undistortion removes lens radial/tangential distortion (Brown–Conrady model).
- Depth can be *inferred* via **stereo** (triangulation from the disparity) or *measured* directly (RGB-D like the depth camera).

### 8.2 Point clouds & ICP

LiDAR/depth produce `PointCloud2`. Alignment/registration between clouds uses **ICP** (same math as §6.3). Object detection runs CNNs (YOLO) on `image_raw`; detections are projected into the robot frame through the intrinsics+extrinsics chain → that's how "I see a person at (x,y)" happens.

---

## 9. Algorithm → ROS2 Package Map

| Theory § | ROS2 implementation |
|---|---|
| §2 transforms | **tf2** (`tf2_ros`, `tf_transformations`) · URDF |
| §2.5 odometry | any odom node → `/odom` |
| §3 dynamics | **Gazebo** (ODE/Bullet/DART) · **ros2_control** |
| §4 PID | `ros2_control` PID controllers · Nav2 controller plugins |
| §4.4 MPC | `nav2` plugins, `mpc_ros` (community) |
| §5 Kalman/EKF | `robot_localization` (EKF/UKF) |
| §5.4 IMU | Mahony/Madgwick filters |
| §5.3 localization | **AMCL** (particle filter) in Nav2 |
| §6 SLAM | **slam_toolbox** · **Cartographer** |
| §7 A*/planners | Nav2 `planner_server` (NavFn/Smac) · `controller_server` (DWA/TEB/MPPI) |
| §8 perception | `cv_bridge`, YOLO nodes, PCL |
| §7/§8 costmaps | Nav2 `costmap_2d` (static/obstacle/inflation layers) |

Next: **[[ros2-architecture]]** — how all of these algorithms become ROS2 nodes.
