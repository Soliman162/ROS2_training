import rclpy
import sys
from rclpy.node import Node
from std_msgs.msg import Int16
from my_interfaces.srv import Addints2


class clientNode(Node):

    def __init__(self):
        super().__init__('client_Node')
        self.cli = self.create_client(Addints2,'add_two_number')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Addints2.Request()

    def send_request(self,a,b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self,self.future)
        return self.future.result()


def main():
    rclpy.init()
    client = clientNode()

    response = client.send_request( int(sys.argv[1]) , int(sys.argv[2]))
    
    client.get_logger().info(
    'Result of add_two_ints: for %d + %d = %d' %
    (int(sys.argv[1]), int(sys.argv[2]), response.sum))

    # rclpy.spin(client)
    rclpy.shutdown()


if __name__ == '__main__':
    main()