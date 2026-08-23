---
tags: [wiki, modules, robotics]
last_updated: "2026-08-17"
---

# ROS2 Cheat Sheet — Commands, Code & Config Reference

> Full quick-reference: environment, CLI, launch, colcon, interfaces, QoS, lifecycle, tracing, and rclpy/rclcpp skeletons. Deep explanations in the linked pages.
> **Related:** [[modules/robotics/index|Robotics & ROS2 Hub]] · [[ros2-tools-debugging]] · [[ros2-beginner-guide]] · [[modules/index|Modules Catalog]] · [[wiki/index|Wiki Home]]

## Environment

```bash
source /opt/ros/jazzy/setup.bash                # underlay (distro)
source ~/ros2_ws/install/setup.bash             # overlay (your workspace)
export ROS_DOMAIN_ID=42                         # network isolation
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp    # DDS vendor (match everywhere)
export ROS_LOCALHOST_ONLY=1                     # single-machine dev
export TURTLEBOT3_MODEL=burger
```

## Nodes & graph

| Command | Action |
|---|---|
| `ros2 run <pkg> <node>` | run a node |
| `ros2 node list` / `ros2 node info <n>` | list / detail |
| `ros2 run <pkg> <node> --ros-args -r old:=new` | remap topic |
| `ros2 run <pkg> <node> --ros-args -p speed:=1.0` | set param on launch |
| `ros2 run rqt_graph rqt_graph` | live graph GUI |

## Topics

| Command | Action |
|---|---|
| `ros2 topic list [-t]` | list (+types) |
| `ros2 topic echo <t>` | stream |
| `ros2 topic info <t> -v` | type + QoS both sides |
| `ros2 topic hz <t>` / `bw <t>` / `delay <t>` | rate / bandwidth / latency |
| `ros2 topic pub <t> <type> "{...}" --once` | publish once |

## Services / Actions / Params / Interfaces

```bash
ros2 service list [-t]
ros2 service call /toggle_power interfaces_pkg/srv/TogglePower "{enable: true}"
ros2 action list [-t]
ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "{pose: {pose: {position: {x: 1.0, y: 2.0, z: 0.0}}}}" --feedback
ros2 param list/get/set/dump <node>
ros2 interface show sensor_msgs/msg/LaserScan
ros2 interface proto geometry_msgs/msg/Twist      # C++/py class layout
ros2 lifecycle list / get / set <node> <state>
```

## colcon (build)

```bash
colcon build --symlink-install                   # default workflow
colcon build --packages-select <pkg>             # one package
colcon build --packages-up-to <pkg>              # pkg + deps
colcon build --packages-above <pkg>              # everything depending on pkg
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release
colcon test --packages-select <pkg> && colcon test-result --verbose
colcon clean build
source install/setup.bash
ros2 pkg create <pkg> --build-type ament_python
ros2 pkg create <pkg> --build-type ament_cmake --dependencies rclcpp std_msgs
```

## Launch files

```python
# launch/demo.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package="my_pkg", executable="my_node",
             name="renamed_node",
             parameters=["config/params.yaml"],     # or [{"speed": 1.0}]
             remappings=[("/old", "/new")]),
    ])
```

```bash
ros2 launch my_pkg demo.launch.py
ros2 launch my_pkg demo.launch.py use_sim_time:=True    # override arg
```

## QoS quick picks

| Scenario | Reliability | Durability | Depth |
|---|---|---|---|
| Camera/LiDAR streams | best_effort | volatile | 5 |
| Commands / state | reliable | volatile | 10 |
| Late-join replay (map, tf, static) | reliable | transient_local | 10+ |
| Lifecycle-critical (switch signals) | reliable | transient_local | 1–10 |

```python
# rclpy
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
qos = QoSProfile(depth=5,
                 reliability=ReliabilityPolicy.BEST_EFFORT)
self.create_subscription(LaserScan, "scan", self.cb, qos)

# rclcpp
auto qos = rclcpp::SensorDataQoS();                 // best_effort + depth 5
sub_ = create_subscription<sensor_msgs::msg::LaserScan>("scan", qos, cb);
```

## rclpy skeleton (with executor + params)

```python
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup

class Node(Node):
    def __init__(self):
        super().__init__("node")
        self.declare_parameter("speed", 0.5)
        self.g = MutuallyExclusiveCallbackGroup()
        self.pub = self.create_publisher(String, "out", 10)
        self.timer = self.create_timer(0.1, self.tick, callback_group=self.g)

    def tick(self):
        msg = String(); msg.data = str(self.get_parameter("speed").value)
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    ex = MultiThreadedExecutor(num_threads=2)
    ex.add_node(Node())
    ex.spin()
```

## rclcpp skeleton

```cpp
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

class Node : public rclcpp::Node {
public:
  Node() : Node("node") {
    declare_parameter("speed", 0.5);
    pub_ = create_publisher<std_msgs::msg::String>("out", 10);
    timer_ = create_wall_timer(std::chrono::milliseconds(100),
        [this]{ auto m=std_msgs::msg::String();
                m.data=std::to_string(get_parameter("speed").as_double());
                pub_->publish(m); });
  }
private:
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr pub_;
  rclcpp::TimerBase::SharedPtr timer_;
};
```

## tf2

```bash
ros2 run tf2_tools view_frames            # frames.pdf
ros2 run tf2_ros tf2_echo map odom
ros2 run rqt_tf_tree rqt_tf_tree
# frames: map → odom → base_link → sensor frames (REP-105)
```

```python
# lookup with timeout (the standard trap)
t = buf.lookup_transform("map", "laser", rclpy.time.Time(),
                         timeout=rclpy.duration.Duration(seconds=1))
```

## rosbag & tracing

```bash
ros2 bag record -a -o run1
ros2 bag play run1 --clock               # + use_sim_time:=true on consumers
ros2 bag info run1

export ROS_TRACE_DIR=$HOME/ros_traces
ros2 trace start ... ros2 trace stop     # LTTng-based latency attribution (CARET/tracetools)
```

## Nav2 (quick)

```bash
# SLAM map → save
ros2 run slam_toolbox online_async_launch.py
ros2 run nav2_map_server map_saver_cli -f ~/my_map
# navigate
ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=~/my_map.yaml
# inspect the pipeline
ros2 action info /navigate_to_pose
ros2 topic echo /cmd_vel | ros2 topic hz /scan
```

## Debug order

```
1 ros2 doctor              4 ros2 topic echo/hz     7 bag replay --clock
2 ros2 node/topic list     5 rqt_graph / console    8 tracing (latency)
3 ros2 topic info <t> -v   6 view_frames / tf2_echo 9 change ONE thing, re-measure
```

## Install one-liner (Jazzy / Ubuntu 24.04)

```bash
sudo apt install -y ros-jazzy-desktop ros-dev-tools \
  ros-jazzy-gazebo-ros-pkgs ros-jazzy-nav2 ros-jazzy-slam-toolbox \
  ros-jazzy-turtlebot3-*
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
```
