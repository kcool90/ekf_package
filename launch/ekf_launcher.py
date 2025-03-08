import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[os.path.join(
                os.path.dirname(__file__),
                'config',
                'ekf.yaml'
            )],
        ),

        Node(
            package='robot_localization',
            executable='navsat_transform_node',
            name='navsat_transform',
            output='screen',
            parameters=[os.path.join(
                os.path.dirname(__file__),
                'config',
                'navsat.yaml'
            )],
            remappings=[
                ('earth/imu/data', '/earth/imu/data'),
                ('earth/gps/fix', '/earth/gps/fix'),
                ('odometry/gps', '/earth/odometry/gps')
            ]
        )

    ])
