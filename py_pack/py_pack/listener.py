import rclpy

from rclpy.node import Node
from std_msgs.msg import String
# from my_interfaces.msg import V2V
#from my_interfaces.srv import TestSum

class subscribe_node(Node):

    def __init__(self):
        super().__init__("lisnter_node")
        self.create_subscription(callback=self.subscriber_callback,msg_type=String,topic='chat',qos_profile=10)

    def subscriber_callback(self,msg):
        self.get_logger().info(f"I heard {msg.data} ")


def main(args=None):
    rclpy.init(args=args)
    subscriber = subscribe_node()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
