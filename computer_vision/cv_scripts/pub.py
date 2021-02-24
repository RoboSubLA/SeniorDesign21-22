#!/usr/bin/env python
# license removed for brevity
import rospy
from computer_vision.msg import Cv_data

def talker():
    pub = rospy.Publisher('chatter', Cv_data, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    data = Cv_data()

    while not rospy.is_shutdown():
        data.object = "Name"
        data.confidence = 99.00
        data.coordinates = 100
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

