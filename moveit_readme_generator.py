#! /usr/bin/python3

packages = [
    "moveit",
    "moveit_ros",
    "moveit_common",
    "moveit_msgs",
    "moveit_core",
    "moveit_servo",
    "moveit_plugins",
    "moveit_runtime",
    "moveit_planners",
    "moveit_resources",
    "moveit_resources_fanuc_description",
    "moveit_resources_fanuc_moveit_config",
    "moveit_resources_panda_description",
    "moveit_resources_panda_moveit_config",
    "moveit_resources_pr2_description",
    "moveit_kinematics",
    "moveit_ros_warehouse",
    "moveit_ros_benchmarks",
    "moveit_ros_move_group",
    "moveit_ros_perception",
    "moveit_ros_planning",
    "moveit_ros_visualization",
    "moveit_ros_occupancy_map_monitor",
    "moveit_ros_planning_interface",
    "moveit_ros_robot_interaction",
    "moveit_setup_app_plugins",
    "moveit_setup_assistant",
    "moveit_setup_controllers",
    "moveit_setup_core_plugins",
    "moveit_setup_framework",
    "moveit_setup_srdf_plugins",
    "moveit_simple_controller_manager",
    "geometric_shapes",
    "warehouse_ros",
    "warehouse_ros_mongo",
    "srdfdom",
    "random_numbers",
    "moveit_planners_ompl",
    "pilz_industrial_motion_planner",
    "pilz_industrial_motion_planner_testutils",
    "moveit_hybrid_planning",
]

packages.sort()

distros = {"Foxy": "focal", "Galactic": "focal", "Rolling": "jammy", "Humble": "jammy"}
jobs = {"bin": "Binary"}

# Packages are not available in these distros
exceptions = {
    "moveit_setup_app_plugins": ["Foxy", "Galactic"],
    "moveit_setup_assistant": ["Foxy", "Galactic"],
    "moveit_setup_controllers": ["Foxy", "Galactic"],
    "moveit_setup_core_plugins": ["Foxy", "Galactic"],
    "moveit_setup_framework": ["Foxy", "Galactic"],
    "moveit_setup_srdf_plugins": ["Foxy", "Galactic"],
    "pilz_industrial_motion_planner": ["Foxy"],
    "pilz_industrial_motion_planner_testutils": ["Foxy"],
    "moveit_hybrid_planning": ["Foxy"],
    "warehouse_ros_mongo": ["Humble", "Rolling"],
}


# The headers
headers = ["MoveIt Package"]
for distro in distros:
    for job_alias in jobs.values():
        headers.append(distro + " " + job_alias)

values = []
for package_no in range(len(packages)):
    row = []
    package = packages[package_no]
    row.append(package)
    for ros_distro, ubuntu_distro in distros.items():
        for job, job_alias in jobs.items():

            # Construct job string
            job_str = ""
            job_str += ros_distro[0]  # First letter of ROS Distro
            job_str += job  # job name
            job_str += "_u"
            job_str += ubuntu_distro[0].upper()  # First letter of Ubuntu Distro
            if job == "bin":
                job_str += "64"
            job_str += "__"
            job_str += package
            job_str += "__ubuntu_"
            job_str += ubuntu_distro
            job_str += "_"
            if job == "bin":
                job_str += "amd64_"
            job_str += "_"
            job_str += job_alias.lower()
            job_str += ")"

            # Construct the actual string
            str = "[![Build Status](https://build.ros2.org/buildStatus/icon?job="
            str += job_str
            str += "](https://build.ros2.org/job/"
            str += job_str

            if package in exceptions.keys():
                if ros_distro in exceptions[package]:
                    str = "N/A"
            row.append(str)
    values.append(row)

f = open("moveit.md", "w")  # write in text mode
f.write("|")
for header in headers:
    f.write(" " + header + " |")
f.write("\n|")
for header in headers:
    f.write(":---:|")

for row in values:
    f.write("\n|")
    for item in row:
        f.write(" ")
        f.write(item)
        f.write(" |")

f.write("\n")
f.close()
