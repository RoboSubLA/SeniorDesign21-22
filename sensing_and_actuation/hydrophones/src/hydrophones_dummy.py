#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import String
from hydrophones.msg import Hydrophones

while True:
    publisher = rospy.Publisher('hydrophones_dummy_topic', Hydrophones, queue_size=10)
    rospy.init_node('hydrophones_dummy')
    rate = rospy.Rate(10)

    hydrophones_msg = Hydrophones()
    hydrophones_msg.direction = 170

    while not rospy.is_shutdown():
        time.sleep(2)
        rospy.loginfo(hydrophones_msg)
        publisher.publish(hydrophones_msg)
    rate.sleep()