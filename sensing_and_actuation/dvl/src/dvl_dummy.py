#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import String
from dvl.msg import DVL

while True:
    publisher = rospy.Publisher('dvl_topic', DVL, queue_size=10)
    rospy.init_node('dvl_dummy')
    rate = rospy.Rate(10)

    dvl_msg = DVL()
    dvl_msg.pitch = 3.2
    dvl_msg.yaw = 0.8
    dvl_msg.roll = 1
    dvl_msg.x_translation = 10
    dvl_msg.y_translation = 12

    while not rospy.is_shutdown():
        time.sleep(2)
        rospy.loginfo(dvl_msg)
        publisher.publish(dvl_msg)
    rate.sleep()