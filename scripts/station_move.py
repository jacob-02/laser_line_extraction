#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from laser_line_extraction.msg import LineSegmentList

def callback(msg):
    motion = Twist()

    f = msg.line_segments[0].radius

    theta_1 = msg.line_segments[0].start[1]
    theta_2 = msg.line_segments[0].end[1]

    orientation = theta_1 - theta_2

    motion.linear.x = 0.2*(f - 0.1)
    motion.angular.z = 0.2*(orientation)

    pub.publish(motion)

rospy.init_node('scan_data_station', anonymous=True)
sub = rospy.Subscriber('/line_segments', LineSegmentList, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
rospy.spin()
