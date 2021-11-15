#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16
from ez_async_data.msg import Barometer
import time
import random

def talker():
    pub = rospy.Publisher('bar_data', Barometer, queue_size=10)
    rospy.init_node('rand_counter', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    counter = 0
    elapsed_time = 0
    start_time = time.time()
    while elapsed_time < 60:
        rospy.loginfo(counter)
        pub.publish(counter)
	counter = random.randint(700,766)
        rate.sleep()
	elapsed_time = time.time() - start_time

    exit()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
