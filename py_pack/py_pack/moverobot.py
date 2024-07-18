import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from my_interfaces.action import Reachwall



class Move_node(Node):
    def __init__(self):
        super().__init__('moving_robot')
        self.action_server = ActionServer(action_name="reach_wall",node=self,action_type=Reachwall,execute_callback=self.goal_callback)
        self.distance_publisher = self.create_publisher(msg_type=Twist,topic="/cmd_vel",qos_profile=10)
        self.sensor_subscriber = self.create_subscription(msg_type=LaserScan,topic="/scan",callback=self.laser_callback,qos_profile=10)


    def laser_callback(self,msg):
        self.distance_from_Wall = min(min(msg.ranges[0:10]),12)

    def goal_callback(self,goal_handle):
        self.get_logger().info(f"recived goal request: {goal_handle.request}")
        feed_msg = Reachwall.Feedback()
        result_msg = Reachwall.Result()
        robot_vel = Twist()

        while self.distance_from_Wall > goal_handle.request.req_distance :
            rclpy.spin_once(self)
            robot_vel.linear.x = 0.1
            feed_msg.remain_distance = self.distance_from_Wall
            goal_handle.publish_feedback(feed_msg)
            self.distance_publisher.publish(robot_vel)
            self.get_logger().info(f"distance_from_Wall: {self.distance_from_Wall}")

        robot_vel.linear.x = 0.0
        self.distance_publisher.publish(robot_vel)
        result_msg.resault = True
        goal_handle.succeed()
        return result_msg


def main():
    rclpy.init()

    robctrl_node = Move_node()

    try:
        rclpy.spin(robctrl_node)
    except KeyboardInterrupt:
        pass
    robctrl_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()