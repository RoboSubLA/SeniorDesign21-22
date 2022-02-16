#!/usr/bin/env python

import rospy
from std_msgs.msg import String

while True:
    publisher = rospy.Publisher('dummy_topic', String, queue_size=10)
    rospy.init_node('dummy_publisher')
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        my_string = 'Hello'
        rospy.loginfo(my_string)
        publisher.publish(my_string)
    rate.sleep()