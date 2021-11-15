#!/usr/bin/env python


# issues when keyboard interrupting this node
# terminal needs to be closed and relaunched

import rospy
import time
import random

# if possible use data type from package
# ignore import error
from ez_async_data.msg import Barometer, Rotation, CV
import threading

from std_msgs.msg import String

stopFlag = False
data_rate = 10

def imu_publisher_thread():
    pub = rospy.Publisher('imu_data', Rotation, queue_size=10)
    rate = rospy.Rate(data_rate)  # 10hz

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
    rate = rospy.Rate(data_rate)  # 10hz

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


def dvl_publisher_thread():
    pub = rospy.Publisher('dvl_data', String, queue_size=10)
    rate = rospy.Rate(data_rate)

    while not rospy.is_shutdown():
        if stopFlag:
            break

        data = random.randint(0, 100)
        pub.publish(str(data))
        rate.sleep()

def cv_publisher_thread():
    pub = rospy.Publisher('cv_data', CV, queue_size=10)
    rate = rospy.Rate(data_rate)

    data = CV()
    data.targetSeen = False
    data.targetDis = -99
    data.xOffset = -99
    data.yOffset = -99

    while not rospy.is_shutdown():
        if stopFlag:
            break

        # data.targetDis = random.randint(0, 100)
        # data.targetdiscenter = random.randint(0, 100)
        # if data.targetDis < 50 and data.targetdiscenter < 50:
        #     data.targetSeen = True

        data.targetSeen = True
        data.targetDis = random.randint(30,50)
        data.xOffset = random.randint(-5,5)
        data.yOffset = random.randint(30,40)
        pub.publish(data)
        rate.sleep()


if __name__ == '__main__':
    rospy.init_node('dummy_instrument_node', anonymous=True)

    imuPub = threading.Thread(target=imu_publisher_thread, args=())
    barPub = threading.Thread(target=barometer_publisher_thread, args=())
    dvlPub = threading.Thread(target=dvl_publisher_thread, args=())
    cvPub = threading.Thread(target=cv_publisher_thread, args=())

    try:
        imuPub.daemon = True
        barPub.daemon = True
        dvlPub.daemon = True
        cvPub.daemon = True

        imuPub.start()
        barPub.start()
        dvlPub.start()
        cvPub.start()

        while True:
            time.sleep(1)

    except rospy.ROSInterruptException:
        stopFlag = False
        time.sleep(1)
        pass

