---
tags: [wiki, modules, robotics]
last_updated: "2026-08-17"
---

# ROS2 Installation & Build System — Distros · colcon · ament · rosidl · Overlays

> From picking a distro to understanding exactly what `colcon build` does. This page goes one layer below "type these commands" into the **build pipeline, package format, env mechanics, and workspace architecture**.
> **Sources:** docs.ros.org (Installation, colcon, ament_cmake docs), ros_core_documentation (developer_overview), ROS answers (dependency mgmt), rosidl/ament GitHub.
> **Related:** [[modules/robotics/index|Robotics & ROS2 Hub]] · [[ros2-beginner-guide]] · [[ros2-tools-debugging]] · [[modules/index|Modules Catalog]] · [[wiki/index|Wiki Home]]

## 1. Distro selection — the release system, understood

ROS2 ships **one distro per year (~May 23)**:

- **Even years → LTS** with **5 years** of support.
- **Odd years → short-term**, supported until Dec of the following year.

| Distro | Released | Support until | Ubuntu | Verdict |
|---|---|---|---|---|
| **Humble Hawksbill** | 2022-05 | **2027-05** | 22.04 | aging LTS; big legacy tutorial base |
| **Jazzy Jalisco** | 2024-05 | **2029-05** | 24.04 | **the 2026 sweet spot** — LTS + current ecosystem |
| **Kilted Kaiju** | 2025-05 | **2026-12** | 24.04 | non-LTS, do not start here |
| **Lyrical Luth** | 2026-05 | **2031-05** | 26.04 | newest LTS; new executor (Events/CBG) landed here; fewer tutorials yet |

> Rule: pick the **newest LTS that your tutorials target** — for 2026 that's **Jazzy**. `Rolling` is the dev release (always newest features, never stable — for contributors, not beginners).

## 2. The build pipeline — what actually runs when you type `colcon build`

```
colcon build
  ├─ discovers packages by finding package.xml under src/
  ├─ topologically sorts them by their dependencies
  ├─ for each package, invokes its build system:
  │     ament_cmake  ─▶ CMake ─▶ native compiler (g++/clang)
  │     ament_python ─▶ setuptools (pip-style)
  │     ament_cmake_python ─▶ both
  └─ installs artifacts into install/<pkg>/ and writes env hooks
```

**Why not plain `make`?** colcon solves **scalability**:
- Dependency order across many packages (it builds `interfaces` before nodes that `find_package()` them).
- Parallel builds with `--executor parallel`.
- Underlay/overlay awareness so it never rebuilds the installed distro.
- Per-package `build/<pkg>`, `install/<pkg>`, `log/latest_build/`.

## 3. The package manifest — `package.xml`

The **marker + metadata** of any ament package (REP-127/140). `colcon` finds packages by crawling for these files.

```xml
<?xml version="1.0"?>
<package format="3">
  <name>my_pkg</name>
  <version>0.1.0</version>
  <description>...</description>
  <maintainer email="...">you</maintainer>
  <license>Apache-2.0</license>

  <buildtool_depend>ament_cmake</buildtool_depend>

  <depend>rclcpp</depend>              <!-- build + run + exec -->
  <depend>std_msgs</depend>
  <build_depend>geometry_msgs</build_depend>
  <exec_depend>ros2launch</exec_depend>
  <test_depend>ament_lint_auto</test_depend>
</package>
```

Dependency types: `buildtool_depend` (ament/cmake), `build_depend` (headers at build), `exec_depend` (runtime libs), `depend` (both), `test_depend` (tests only).

**Why both package.xml AND CMakeLists?** (the classic student question)
- `package.xml` = machine-readable **manifest** → colcon ordering, `rosdep` (resolve deps to `apt`), release tooling (bloom), CI. CMake can't know about the *whole* workspace.
- `CMakeLists.txt` = actual **build recipe** for *this* package (`find_package` + compile + link + install).

## 4. ament_cmake anatomy

```cmake
cmake_minimum_required(VERSION 3.8)
project(my_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)          # + std_msgs, sensor_msgs, ...
find_package(rosidl_default_generators REQUIRED)  # if you define interfaces

add_library(my_lib src/core.cpp)                    # optionally a lib
ament_target_dependencies(my_lib rclcpp std_msgs)   # includes/libs/flags in one call

rosidl_generate_interfaces(my_pkg
  "msg/MyData.msg" "srv/MySrv.srv" "action/MyAct.action"
  DEPENDENCIES std_msgs geometry_msgs
)

install(TARGETS my_lib DESTINATION lib)
install(DIRECTORY launch config DESTINATION share/${PROJECT_NAME})
ament_package()
```

- `ament_target_dependencies` replaces hand-rolling `target_include_directories`/`target_link_libraries` — it injects the right flags from the dependency's `ament index`.
- `ament_auto_*` macros (`ament_auto_find_build_dependencies`) automate find/compile for simple packages.
- **The ament index**: install trees keep a small index (`share/ament_index`) so tools/environment hooks can discover packages without scanning disk — this is *why* your Python/Ros2 packages resolve.

## 5. rosidl — interfaces become code

```
msg/srv/action ──(rosidl parser)──▶ IDL ──(generators)──▶ C / C++ / Python classes
   MyData.msg                      rosidl_generator_cpp  rosidl_generator_py ...
```

- **Build-time code generation**: your `.msg` compiles into real classes (`pkg::msg::MyData`, `pkg.msg.MyData`).
- **Extension mechanism**: third-party languages (ros2_rust, ros2_java) plug in their own generator packages; the pipeline is CMake-coupled today (rosidl #560) but the parser/generators are language-neutral libraries.
- Interfaces live in **their own package** → consumers share one ABI. Change a field = ABI break → rebuild all dependents. **Never** put interfaces in a node package if you care about reuse.

## 6. Underlay / overlay — how sourcing works

```
                    ┌──────── overlay: ~/ros2_ws/install  (your packages)
                    │          ↑ overrides
underlay: /opt/ros/jazzy  (the distro)
```

Sourcing `install/setup.bash` **prepends** to a chain of env vars:

| Var | What it feeds |
|---|---|
| `AMENT_PREFIX_PATH` | list of install prefixes → ament index lookup |
| `PYTHONPATH` | importable Python packages |
| `LD_LIBRARY_PATH` (Linux) / `PATH` | shared libs & binaries |
| `ROS_PACKAGE_PATH` | resource/launch discovery |

The overlay shadows the underlay for same-named packages — that's how you can patch a distro package without touching `/opt`. **Every new terminal** must re-source both underlay and overlay (put both in `~/.bashrc`).

## 7. Python packages under ament

`ament_python` = setuptools. `setup.py`:

```python
from setuptools import setup
package_name = 'py_pubsub'
setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', [f'resource/{package_name}']),
        (f'share/{package_name}', ['package.xml']),
        (f'share/{package_name}/launch', ['launch/demo.launch.py']),
    ],
    entry_points={'console_scripts': ['talker = py_pubsub.publisher:main']},
)
```

The `data_files` rows register the package in the **ament index** (so `ros2 pkg`/launch find it) — forgetting them is the #1 "package builds but `ros2 run` says not found" bug.

## 8. Build commands that matter

```bash
colcon build                                        # everything
colcon build --symlink-install                      # Python hot-reload (no rebuild)
colcon build --packages-select my_pkg               # just one package
colcon build --packages-up-to my_pkg                # pkg + its workspace deps
colcon build --packages-above my_pkg                # everything depending on pkg
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release  # pass through to CMake
colcon test --packages-select my_pkg && colcon test-result --verbose
colcon clean build                                  # nuke build+install
source install/setup.bash
```

## 9. Dependencies: apt, rosdep, and from-source

```bash
sudo apt install ros-jazzy-nav2 ros-jazzy-slam-toolbox   # binary packages
rosdep install -y --from-paths src --ignore-src          # resolve package.xml deps
```

- **Binary install** (apt) = distro packages; **source install** (colcon from git) = everything else. Mixing: overlay source packages on top of the apt underlay.
- Fleet/release workflows: `rosinstall_generator` + `vcstool` to pin repos/commits, `bloom` to release new versions.

## 10. Installation checklist (engineering edition)

- [ ] Ubuntu 24.04 + `ros-jazzy-desktop` + `ros-dev-tools`
- [ ] `talker`/`listener` demo passes in two terminals
- [ ] Understand underlay vs overlay; `.bashrc` sources both
- [ ] First package builds with `colcon build --symlink-install`
- [ ] A custom interface package builds and `ros2 interface show` prints it
- [ ] A launch file runs (see [[ros2-beginner-guide]])

Next: **[[ros2-beginner-guide]]** — the full hands-on build, now with rclcpp + rclpy, executors, tf2/URDF and Nav2 internals.
