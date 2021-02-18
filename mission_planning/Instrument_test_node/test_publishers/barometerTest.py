#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16, String
import time
import threading
import numpy


def callback(data):
    barometer = data
    rospy.loginfo(str(barometer) + ' atm')


def barometerTest():
    rospy.init_node('listener', anonymous=True)
    sub = rospy.Subscriber("data_pub_input", Int16, callback)
    pub = rospy.Publisher("data_recorder", String, queue_size=20)
    pub.publish(sub)
    rospy.spin()



if __name__ == '__main__':
    barometerTest()
    # make pub
    # wait for data
    # if vaild return true
    # else false
