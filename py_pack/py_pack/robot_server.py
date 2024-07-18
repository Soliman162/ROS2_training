import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from coppeliasim_zmqremoteapi_client import *


class robotCrtl(Node):
    def __init__(self):
        super().__init__("robot_control")
        self.create_subscription(callback=ctrlRobot(),topic="robot",msg_type=Pose2D)


    def ctrlRobot(self,position):
        pass




def main():
    rclpy.init()


    rclpy.shutdown()




if __name__ == '__main__':
    main()