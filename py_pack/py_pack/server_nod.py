import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from my_interfaces.srv import Addints2


class serverNode(Node):

    def __init__(self):
        super().__init__('server_Node')
        self.service = self.create_service(Addints2,"add_two_number",self.add_sum)

    def add_sum(self,request,response):
        response.sum = request.a +request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
        return response


def main():
    rclpy.init()
    service = serverNode()
    rclpy.spin(service)
    service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()