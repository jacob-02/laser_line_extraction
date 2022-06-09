#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    new = msg
    # ind = [330, 390]
    newData = list(msg.ranges);
    # print(len(msg.ranges))
    for i in range(len(msg.ranges)):
        if (i <= 309 or i >= 410):
            newData[i] = 0
        
        if (msg.ranges[i] >= 1.2):
            newData[i] = 0


    new.ranges = tuple(newData)
    pub.publish(new)



rospy.init_node('new_scan', anonymous=True)
sub = rospy.Subscriber('/scan', LaserScan, callback=callback)
pub = rospy.Publisher('/station_scan', LaserScan, queue_size=2)
rospy.spin()