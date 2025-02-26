import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Path to the package's share directory
    pkg_share = get_package_share_directory('iai_apartment')

    # Path to the URDF file
    urdf_file = os.path.join(pkg_share, 'urdf', 'apartment.urdf')

    # Static transform publisher for the apartment root link
    static_transform_publisher = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='iai_apartment_root_link_broadcaster',
        arguments=['0', '0', '0', '0', '0', '0', 'map', 'iai_apartment/apartment_root'],
        output='screen',
    )

    # Load the URDF file into the parameter server
    apartment_description = Node(
        package='xacro',
        executable='xacro',
        name='xacro',
        arguments=[urdf_file],
        output='screen',
        parameters=[{'robot_description': 'apartment_description'}],
    )

    # Robot state publisher for the apartment
    apartment_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='apartment_state_publisher',
        output='screen',
        parameters=[{'robot_description': 'apartment_description'}],
        remappings=[
            ('robot_description', 'apartment_description'),
            ('joint_states', 'apartment_joint_states'),
        ],
    )

    # Joint state publisher for the apartment
    apartment_joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='apartment_joint_state_publisher',
        output='screen',
        parameters=[{'rate': 25}],
        remappings=[
            ('robot_description', 'apartment_description'),
            ('joint_states', 'apartment_joint_states'),
        ],
    )

    # Joint state publisher GUI
    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen',
        remappings=[
            ('robot_description', 'apartment_description'),
            ('joint_states', 'iai_kitchen/cram_joint_states'),
        ],
    )

    # RViz2 node
    rviz_config_file = os.path.join(pkg_share, 'rviz_config', 'rviz_config.rviz')
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
    )

    # Launch description
    return LaunchDescription([
        static_transform_publisher,
        apartment_description,
        apartment_state_publisher,
        apartment_joint_state_publisher,
        joint_state_publisher_gui,
        rviz_node,
    ])