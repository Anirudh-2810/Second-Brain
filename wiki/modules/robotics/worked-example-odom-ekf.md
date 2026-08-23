---
tags: [wiki, modules, robotics]
last_updated: "2026-08-17"
---

# Worked Example — Differential-Drive Odometry + EKF in rclpy

> The derivations from [[robotics-fundamentals]] §2.5 and §5 applied, end-to-end, in runnable rclpy: a **differential-drive odometry node** (unicycle model, tf2 publishing), a **2D EKF** fusing odometry + IMU yaw, and a **fake-robot simulator** to run and verify it with no hardware.
> **Sources:** [[robotics-fundamentals]] (derivations), `robot_localization` docs (production equivalent), docs.ros.org tutorials.
> **Related:** [[modules/robotics/index|Robotics & ROS2 Hub]] · [[robotics-fundamentals]] · [[ros2-beginner-guide]] · [[modules/index|Modules Catalog]] · [[wiki/index|Wiki Home]]

## 1. The System

```mermaid
flowchart LR
    S[fake_robot<br/>simulator<br/>(ground truth)] -->|joint_states<br/>wheel ω_L ω_R| O[odometry_node<br/>unicycle model]
    S -->|imu<br/>yaw θ + noise| E[ekf_node<br/>2D EKF]
    O -->|odom<br/>v, ω + pose| E
    E -->|odom_ekf<br/>fused state + covariance| V[PlotJuggler / RViz]
```

Three nodes, one topic graph. The **fake robot** publishes exactly what a real robot's encoders + IMU would: noisy wheel velocities and a noisy yaw. The odometry node turns wheel speeds into a pose (open-loop). The EKF fuses it all into a *belief* with covariance. No hardware required.

## 2. The Math You're Implementing (recap from [[robotics-fundamentals]])

**Wheel velocities → robot velocity** (differential drive, wheel radius `r`, wheel base `L`):

```
v    = r·(ω_R + ω_L)/2            forward speed
ω_rob= r·(ω_R − ω_L)/L            angular rate
```

**Unicycle model, integrated with midpoint-Euler** (this is the odometry node):

```
θ_mid = θ + ω·Δt/2
x[k+1] = x[k] + v·Δt·cos(θ_mid)
y[k+1] = y[k] + v·Δt·sin(θ_mid)
θ[k+1] = θ[k] + ω·Δt
```

**EKF** — state `x = [x, y, θ]ᵀ`, control `u = [v, ω]ᵀ` (from odom twist), measurement `z = [x_odom, y_odom, yaw_imu]ᵀ`:

```
PREDICT   x̂⁻ = f(x̂, u)                     (nonlinear unicycle step)
          P⁻ = F·P·Fᵀ + Q                    (F = ∂f/∂x)
UPDATE    K = P⁻Hᵀ(H P⁻Hᵀ + R)⁻¹            (H = I here)
          x̂ = x̂⁻ + K(z − Hx̂⁻)               (innovation: y = z − Hx̂⁻)
          P = (I − K H) P⁻

with F = ┌ 1   0   −v·Δt·sinθ ┐
         │ 0   1    v·Δt·cosθ │
         └ 0   0      1       ┘
```

The only "tuning knobs" in the whole system are **Q** (process noise: how much you trust the model) and **R** (measurement noise: how much you trust each sensor). Bigger Q → filter trusts the measurements; bigger R → filter trusts the model.

## 3. Node 1 — Odometry (differential drive)

`odometry_node.py`:

```python
import math
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import JointState
from geometry_msgs.msg import TransformStamped, Quaternion
from tf2_ros import TransformBroadcaster


def quat_from_yaw(yaw: float) -> Quaternion:
    q = Quaternion()
    q.z = math.sin(yaw / 2.0)
    q.w = math.cos(yaw / 2.0)
    return q


class DifferentialOdometry(Node):
    def __init__(self):
        super().__init__("odometry_node")
        self.declare_parameter("wheel_radius", 0.033)   # r [m]
        self.declare_parameter("wheel_base", 0.160)     # L [m]
        self.r = self.get_parameter("wheel_radius").value
        self.L = self.get_parameter("wheel_base").value

        self.sub = self.create_subscription(JointState, "joint_states", self.on_joint_states, 10)
        self.pub = self.create_publisher(Odometry, "odom", 10)
        self.tfb = TransformBroadcaster(self)

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.last_t = None

    def on_joint_states(self, msg: JointState):
        try:
            iL, iR = msg.name.index("left_wheel_joint"), msg.name.index("right_wheel_joint")
        except ValueError:
            return
        wL, wR = msg.velocity[iL], msg.velocity[iR]       # rad/s
        vL, vR = self.r * wL, self.r * wR                 # m/s

        now = self.get_clock().now()
        if self.last_t is not None:
            dt = (now - self.last_t).nanoseconds * 1e-9
            if dt > 0:
                self.integrate(vL, vR, dt)
        self.last_t = now

    def integrate(self, vL: float, vR: float, dt: float):
        # --- the derivation, applied ----------------------------------
        v = (vR + vL) / 2.0
        omega = (vR - vL) / self.L
        theta_mid = self.theta + omega * dt / 2.0            # midpoint Euler
        self.x += v * dt * math.cos(theta_mid)
        self.y += v * dt * math.sin(theta_mid)
        self.theta = math.atan2(math.sin(self.theta + omega * dt),
                                math.cos(self.theta + omega * dt))  # wrap to [-π, π]
        # -----------------------------------------------------------------
        self.publish_odom(v, omega)

    def publish_odom(self, v: float, omega: float):
        stamp = self.get_clock().now().to_msg()
        odom = Odometry()
        odom.header.stamp = stamp
        odom.header.frame_id = "odom"
        odom.child_frame_id = "base_link"
        odom.pose.pose.position.x = self.x
        odom.pose.pose.position.y = self.y
        odom.pose.pose.orientation = quat_from_yaw(self.theta)
        odom.twist.twist.linear.x = v
        odom.twist.twist.angular.z = omega
        self.pub.publish(odom)

        t = TransformStamped()                                # odom → base_link tf
        t.header.stamp = stamp
        t.header.frame_id = "odom"
        t.child_frame_id = "base_link"
        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.rotation = quat_from_yaw(self.theta)
        self.tfb.sendTransform(t)


def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(DifferentialOdometry())
    rclpy.shutdown()
```

What to notice:
- **Midpoint Euler** (`theta_mid`) is the accuracy upgrade over plain Euler: it evaluates `θ` at the *middle* of the step, giving O(Δt²) accuracy for free.
- The yaw is **wrapped** every step — `atan2(sin, cos)` — so a robot spinning forever never overflows.
- Publishing **tf** (`odom → base_link`) is mandatory; it's what every consumer (AMCL, planners) needs ([[ros2-beginner-guide]] Step 6).

## 4. Node 2 — The EKF

`ekf_node.py`:

```python
import math
import numpy as np
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion


def yaw_from_quat(q: Quaternion) -> float:
    """Yaw (rotation about z) from a quaternion, in [-π, π]."""
    return math.atan2(2.0 * (q.w * q.z + q.x * q.y),
                      1.0 - 2.0 * (q.y**2 + q.z**2))


def wrap(a: float) -> float:
    return math.atan2(math.sin(a), math.cos(a))


class UnicycleEKF(Node):
    def __init__(self):
        super().__init__("ekf_node")
        # Q and R ARE the whole tuning story. Bigger q = trust sensors more.
        self.declare_parameter("q_v", 0.05)      # process noise (linear) [m/s]
        self.declare_parameter("q_w", 0.10)      # process noise (angular) [rad/s]
        self.declare_parameter("r_xy", 0.02)     # odometry position noise [m]
        self.declare_parameter("r_yaw", 0.02)    # IMU yaw noise [rad]

        self.create_subscription(Odometry, "odom", self.on_odom, 10)
        self.create_subscription(Imu, "imu", self.on_imu, 10)
        self.pub = self.create_publisher(Odometry, "odom_ekf", 10)

        self.x = np.zeros(3)                 # [x, y, theta]
        self.P = np.eye(3) * 1e-3            # initial covariance
        self.v, self.w = 0.0, 0.0            # control input u = [v, w]
        self.z_pos = None                    # odom position measurement
        self.z_yaw = None                    # imu yaw measurement
        self.last_t = None

    def on_odom(self, msg: Odometry):
        self.v = msg.twist.twist.linear.x
        self.w = msg.twist.twist.angular.z
        self.z_pos = np.array([msg.pose.pose.position.x, msg.pose.pose.position.y])
        now = self.get_clock().now()
        if self.last_t is not None and self.z_yaw is not None:
            dt = (now - self.last_t).nanoseconds * 1e-9
            if dt > 0:
                self.predict(dt)
                self.update(np.array([self.z_pos[0], self.z_pos[1], self.z_yaw]))
        self.last_t = now

    def on_imu(self, msg: Imu):
        self.z_yaw = yaw_from_quat(msg.orientation)

    def predict(self, dt: float):
        v, w = self.v, self.w
        th = self.x[2]
        # nonlinear process model: unicycle step
        self.x[0] += v * dt * math.cos(th)
        self.x[1] += v * dt * math.sin(th)
        self.x[2] = wrap(self.x[2] + w * dt)
        # Jacobian F = ∂f/∂x evaluated at current state
        F = np.array([[1.0, 0.0, -v * dt * math.sin(th)],
                      [0.0, 1.0,  v * dt * math.cos(th)],
                      [0.0, 0.0,  1.0]])
        qv, qw = self.get_parameter("q_v").value, self.get_parameter("q_w").value
        Q = np.diag([qv**2, qv**2, qw**2]) * dt
        self.P = F @ self.P @ F.T + Q

    def update(self, z: np.ndarray):
        H = np.eye(3)
        rxy, ryaw = self.get_parameter("r_xy").value, self.get_parameter("r_yaw").value
        R = np.diag([rxy**2, rxy**2, ryaw**2])
        S = H @ self.P @ H.T + R
        K = self.P @ H.T @ np.linalg.inv(S)
        y = z - H @ self.x
        y[2] = wrap(y[2])                     # wrap the yaw innovation!
        self.x = self.x + K @ y
        self.P = (np.eye(3) - K @ H) @ self.P
        self.publish()

    def publish(self):
        odom = Odometry()
        odom.header.stamp = self.get_clock().now().to_msg()
        odom.header.frame_id = "odom"
        odom.child_frame_id = "base_link"
        odom.pose.pose.position.x = self.x[0]
        odom.pose.pose.position.y = self.x[1]
        odom.pose.covariance[0] = self.P[0, 0]      # report the belief, not just the point
        odom.pose.covariance[7] = self.P[1, 1]
        odom.pose.covariance[35] = self.P[2, 2]
        self.pub.publish(odom)


def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(UnicycleEKF())
    rclpy.shutdown()
```

The two subtleties an engineer must not miss:
1. **Wrapping the innovation** `y[2]` — if the robot's true heading is +179° and the measurement is −179°, the raw innovation is −358° (huge, wrong); wrapped it's +2° (correct). Skipping this step makes the EKF catastrophically wrong at heading wrap points.
2. **Publishing covariance** — the point estimate is useless without its uncertainty. Consumers (planners, safety monitors) read `pose.covariance` to know how much to trust it.

## 5. Node 3 — The fake robot (simulation = model, applied)

Same unicycle math, run forward with **added noise**, publishing exactly what a real robot's drivers would:

```python
import math
import random
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState, Imu
from geometry_msgs.msg import Quaternion


class FakeRobot(Node):
    def __init__(self):
        super().__init__("fake_robot")
        self.declare_parameter("wheel_radius", 0.033)
        self.declare_parameter("wheel_base", 0.160)
        self.r = self.get_parameter("wheel_radius").value
        self.L = self.get_parameter("wheel_base").value

        self.declare_parameter("noise_wheel", 0.05)      # rad/s of wheel noise
        self.declare_parameter("noise_yaw", 0.05)        # rad of yaw noise
        self.nw = self.get_parameter("noise_wheel").value
        self.ny = self.get_parameter("noise_yaw").value

        self.pub_joints = self.create_publisher(JointState, "joint_states", 10)
        self.pub_imu = self.create_publisher(Imu, "imu", 10)
        self.pub_gt = self.create_publisher(Imu, "ground_truth", 10)

        self.true = np.zeros(3)          # ground-truth [x, y, theta]
        self.t_last = self.get_clock().now()
        self.t = 0.0                     # scripted-trajectory clock
        self.timer = self.create_timer(0.02, self.tick)    # 50 Hz

    def scripted_wheel_speeds(self):
        """A trajectory: straight, turn left, straight, turn right, repeat."""
        phase = self.t % 20.0
        if phase < 8.0:
            wl, wr = 3.0, 3.0            # straight
        elif phase < 12.0:
            wl, wr = 2.0, 4.0            # left arc
        elif phase < 18.0:
            wl, wr = 3.0, 3.0            # straight
        else:
            wl, wr = 4.0, 2.0            # right arc
        return wl, wr

    def tick(self):
        now = self.get_clock().now()
        dt = (now - self.t_last).nanoseconds * 1e-9
        self.t_last = now
        if dt <= 0:
            return
        self.t += dt

        # 1) true dynamics (same unicycle model as the odometry node)
        wl, wr = self.scripted_wheel_speeds()
        v = self.r * (wl + wr) / 2.0
        omega = self.r * (wr - wl) / self.L
        th = self.true[2]
        self.true[0] += v * dt * math.cos(th)
        self.true[1] += v * dt * math.sin(th)
        self.true[2] = math.atan2(math.sin(th + omega * dt), math.cos(th + omega * dt))

        # 2) publish NOISY sensor readings (what a real robot sees)
        nwl = wl + random.gauss(0.0, self.nw)
        nwr = wr + random.gauss(0.0, self.nw)
        js = JointState()
        js.header.stamp = now.to_msg()
        js.name = ["left_wheel_joint", "right_wheel_joint"]
        js.velocity = [nwl, nwr]
        self.pub_joints.publish(js)

        yaw = self.true[2] + random.gauss(0.0, self.ny)
        q = Quaternion()
        q.z = math.sin(yaw / 2.0)
        q.w = math.cos(yaw / 2.0)
        imu = Imu()
        imu.header.stamp = now.to_msg()
        imu.header.frame_id = "base_link"
        imu.orientation = q
        self.pub_imu.publish(imu)

        # 3) publish CLEAN ground truth for verification only
        gt = Imu()
        gt.header.stamp = now.to_msg()
        gt.header.frame_id = "odom"
        gt.linear_acceleration.x = self.true[0]   # abusing fields to carry x, y
        gt.linear_acceleration.y = self.true[1]
        gt.angular_velocity.z = self.true[2]
        self.pub_gt.publish(gt)


def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(FakeRobot())
    rclpy.shutdown()
```

## 6. Build, run, and verify

```bash
mkdir -p ~/ros2_ws/src/odom_ekf_demo/odom_ekf_demo
# drop the three nodes + setup.py + package.xml per [[ros2-installation-setup]] §7
colcon build --packages-select odom_ekf_demo --symlink-install
source install/setup.bash

ros2 run odom_ekf_demo fake_robot        # terminal 1
ros2 run odom_ekf_demo odometry_node     # terminal 2
ros2 run odom_ekf_demo ekf_node          # terminal 3
```

**Verify:**
- `ros2 topic echo /odom_ekf` — fused pose + covariance.
- `ros2 run plotjuggler plotjuggler` — plot `/ground_truth` vs `/odom` vs `/odom_ekf` position: you'll see raw odometry **drift** while the EKF tracks truth.
- **The experiment that proves the concept:** set `noise_yaw` high and `r_yaw` low, or set `q_v`/`q_w` to zero (model perfectly trusted) — the filter will diverge from truth, showing you the exact failure mode of open-loop dead reckoning.

## 7. What this maps to in production

| This example | Production equivalent |
|---|---|
| `odometry_node` | any wheel-odometry driver (TurtleBot3 `turtlebot3_node`, `differential_drive_controller` in ros2_control) |
| `ekf_node` | **`robot_localization`** EKF/UKF (`ekf_node.yaml`, supports odom+imu+gps, 3D state, 15-DOF state vector) |
| `fake_robot` | Gazebo + `gazebo_ros_diff_drive` plugin |
| Ground-truth check | `rosbag` replay + `PlotJuggler` overlay |

`robot_localization` does exactly the math here (more dimensions, more sensors) — but now you can read *why* its YAML has `process_noise_covariance`, `pose0`, `twist0`, and `odom0` blocks.

## 8. Exercises (check your understanding)

1. **Add a GPS** measurement (2D position, noisier than odom) to the update — how do the `R` entries change the fused path?
2. **Explain** why removing the `wrap(y[2])` line causes failure exactly when the robot crosses ±π.
3. **Tune**: hold ground truth fixed and find `q_v/q_w/r_yaw` values that minimize mean tracking error — you've just done EKF tuning by hand.
4. **Scale**: swap the plain-Euler integration in `integrate()` for midpoint (already done) and observe the difference in drift over a long run.

Next: **[[ros2-tools-debugging]]** for measuring this system, or **[[robotics-fundamentals]]** to re-derive the theory.
