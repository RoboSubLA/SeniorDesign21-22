#!/usr/bin/env python


#issues when keyboard interrupting this node
#terminal needs to be closed and relaunched

import rospy
import time
import random

#if possible use data type from package
#ignore import error
from ez_async_data.msg import Rotation
from ez_async_data.msg import Barometer
import threading
# from std_msgs.msg import String

stopFlag = False


def imu_publisher_thread():
    pub = rospy.Publisher('imu_data', Rotation, queue_size=10)
    rate = rospy.Rate(500) # 10hz

    max_pitch = 15
    max_roll = 15
    max_yaw = 40

    pitch_direction = 1
    yaw_direction = 1
    roll_direction = 1

    data = Rotation()
    data.pitch = 0
    data.yaw = 0
    data.roll = 0
    while not rospy.is_shutdown():
        if stopFlag:
            break

        data.pitch = data.pitch + pitch_direction
        if data.pitch >= max_pitch or data.pitch <= -max_pitch:
            pitch_direction = -pitch_direction

        data.roll = data.roll + roll_direction
        if data.roll >= max_roll or data.roll <= -max_roll:
            roll_direction = -roll_direction

        data.yaw = data.yaw + yaw_direction
        if data.yaw >= max_yaw or data.yaw <= -max_yaw:
            yaw_direction = -yaw_direction

        pub.publish(data)
        rate.sleep()

def barometer_publisher_thread():
    pub = rospy.Publisher('bar_data', Barometer, queue_size=10)
    rate = rospy.Rate(500) # 10hz

    data = Barometer()
    data.atm = 0

    while not rospy.is_shutdown():
        if stopFlag:
            break

        data.atm = random.randint(700, 766)
        # bar_string = "Barometer %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('dummy_instrument_node', anonymous=True)

    imuPub = threading.Thread(target=imu_publisher_thread, args=())
    barPub = threading.Thread(target=barometer_publisher_thread, args=())

    try:
        imuPub.daemon = True
        barPub.daemon = True

        imuPub.start()
        barPub.start()

        while True:
            time.sleep(1)

    except rospy.ROSInterruptException:
        stopFlag = False
        time.sleep(1)
        pass

    rospy.spin()
