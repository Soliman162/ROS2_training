import rclpy
import sys
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan 
from my_interfaces.action import Reachwall 

class Client_actionNode(Node):
    def __init__(self):
        super().__init__("client_Action")
        self.cli = ActionClient(action_name="reach_wall",node=self,action_type=Reachwall)


    def send_goal(self,distance):
        goal_msg = Reachwall.Goal()
        goal_msg.req_distance = float(distance)
        
        self.get_logger().info("wait server")
        self.cli.wait_for_server()
        self.send_goalFeature = self.cli.send_goal_async(goal_msg)
        self.send_goalFeature.add_done_callback(self.goal_response_callBack)

    def goal_response_callBack(self,future):
        goal_handel = future.result()

        if not goal_handel.accepted:
            self.get_logger().info("not accepted")
            return
        self.get_logger().info("accepted")

        self.get_result = goal_handel.get_result_async()
        self.get_result.add_done_callback(self.resultCallBack)

    def resultCallBack(self,future):
        resault = future.result().result
        self.get_logger().info('Result: {0}'.format(resault.resault))
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    client = Client_actionNode()
    client.send_goal(sys.argv[1])
    rclpy.spin(client)
    
if __name__ == "__main__":
    main()