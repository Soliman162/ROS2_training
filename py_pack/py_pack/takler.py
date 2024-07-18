import rclpy
from rclpy.node import Node
from std_msgs.msg import String
# from my_interfaces.msg import V2V
#from my_interfaces.srv import TestSum


class Pub_Node(Node):

    def __init__(self):
        self.counter = 0
        super().__init__("talker_Node")
        self.publisher = self.create_publisher(topic="chat",msg_type=String,qos_profile=10)
        self.create_timer(callback=self.timer_callback,timer_period_sec=1.0)
    
    def timer_callback(self):
        msg = String()
        msg.data = "555" #(f"test ros2 node counter {self.counter}") 
        self.publisher.publish(msg)
        self.get_logger().info(f"{msg.data}") 
        self.counter += 1 

def main(args=None):
    rclpy.init(args=args)
    node = Pub_Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()