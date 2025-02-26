import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Path to the package's share directory
    pkg_share = get_package_share_directory('chemistry_laboratory')

    # Path to the URDF file (replace with your URDF or Xacro file)
    #urdf_file = os.path.join(pkg_share, 'urdf', 'robot.urdf')

    # Path to the RViz2 configuration file (optional)
    #rviz_config_file = os.path.join(pkg_share, 'rviz', 'visualize.rviz')

    # Start robot_state_publisher to publish the robot's state
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        #arguments=[urdf_file],
    )

    # Start RViz2 with the specified configuration file
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        #arguments=['-d', rviz_config_file],
    )

    # Launch description
    return LaunchDescription([
        robot_state_publisher_node,
        rviz_node,
    ])