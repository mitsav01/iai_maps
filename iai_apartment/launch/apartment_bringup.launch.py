import os

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro


def generate_launch_description():
    package_dir = get_package_share_directory('iai_apartment')
    apartment_xacro = os.path.join(package_dir, 'urdf', 'apartment.xacro')
    doc = xacro.process_file(apartment_xacro)
    apartment_desc = doc.toprettyxml(indent='  ')
    params = {"robot_description": apartment_desc}

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[params]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
        ),
    ])