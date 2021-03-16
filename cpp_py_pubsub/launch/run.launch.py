from launch import LaunchDescription
from launch_ros.actions import Node
from tracetools_launch.action import Trace

def generate_launch_description():
    return LaunchDescription([
        Trace(
            session_name='cpp_py_pubsub',
            events_kernel=[]
        ),
        Node(
            package='cpp_talker',
            executable='talker',
        ),
        Node(
            package='py_listener',
            executable='listener'
        )
    ])
