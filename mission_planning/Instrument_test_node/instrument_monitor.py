#!/usr/bin/env python
import rospy
import time

from ez_async_data.msg import Rotation
from mission_planning.msg import InstrumentStatus

from threading import Lock

RECEIVED = 'received'


mutex = Lock()

imuData = {'yaw':0, 'pitch':0, 'roll':0, 'time':10, 'received':False}

def imu_callback(data):
    #copy the data using mutex to not intefere
    mutex.acquire()
    imuData['yaw'] = data.yaw
    imuData['pitch'] = data.pitch
    imuData['roll'] = data.roll
    imuData['time'] = time.time()
    imuData[RECEIVED] = True
    mutex.release()
    #processing of the data to be done after data copying
    #if data is invalid set the imuData['recieved'] to false
    # rospy.loginfo(str(barometer) + ' atm')

# def dvl_callback(data):
#     barometer = data
#     rospy.loginfo(str(barometer) + ' atm')

# def cv_callback(data):
#     barometer = data
#     rospy.loginfo(str(barometer) + ' atm')

# def bar_callback(data):
#     barometer = data
#     rospy.loginfo(str(barometer) + ' atm')

def main():
    rospy.init_node('tester', anonymous=True)
    imu_sub = rospy.Subscriber("imu_data", Rotation, imu_callback)
    # sub = rospy.Subscriber("cv_data", Int16, callback)
    # sub = rospy.Subscriber("bar_data", Int16, callback)
    # sub = rospy.Subscriber("dvl_data", Int16, callback)
    pub = rospy.Publisher("instrument_tests", InstrumentStatus, queue_size=1)

    #data container that holds what is to be published
    instrumentData = InstrumentStatus()

    #loop rate of main loop
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        
        #invalidate the incoming data if last recieved is longer that minimum
        if time.time() - imuData['time'] >= .01:
            mutex.acquire()
            imuData[RECEIVED] = False
            mutex.release()

        #publish the current status of all instruments
        mutex.acquire()
        instrumentData.imu = imuData[RECEIVED]
        mutex.release()
        pub.publish(instrumentData)

        rate.sleep()

if __name__ == '__main__':
    main()
