import rospy
import time
from ez_async_data.msg import Barometer, Rotation, CV, test
from std_msgs.msg import String

instrument_test = test()
instrument_test.imu = False
instrument_test.bar = False
instrument_test.cv = False
instrument_test.dvl = False
imuDataTime = 0
dvlDataTime = 0
cvDataTime = 0
barDataTime = 0


def imu_callback(data):
    global imuDataTime
    imuDataTime = time.time()
    instrument_test.imu = True
    rospy.loginfo("Pitch: %d, Yaw: %d, Roll: %d", data.pitch, data.yaw, data.roll)


def dvl_callback(data):
    global dvlDataTime
    dvlDataTime = time.time()
    instrument_test.dvl = True
    rospy.loginfo('dvl: ' + str(data))


def cv_callback(data):
    global cvDataTime
    cvDataTime = time.time()
    instrument_test.cv = True
    rospy.loginfo("targetSeen: %d, targetDis: %d, targetdiscenter: %d",
                  data.targetSeen, data.targetDis, data.targetdiscenter)


def bar_callback(data):
    # barometer data should register the average atm of a standard swimming pool (~700 - 770)
    global barDataTime
    barDataTime = time.time()
    instrument_test.bar = True
    rospy.loginfo('Barometer: ' + str(data.atm) + ' atm')


def main():
    rospy.init_node('tester', anonymous=True)
    rate = rospy.Rate(50)

    rospy.Subscriber("imu_data", Rotation, imu_callback)
    rospy.Subscriber("cv_data", CV, cv_callback)
    rospy.Subscriber("bar_data", Barometer, bar_callback)
    rospy.Subscriber("dvl_data", String, dvl_callback)
    pub = rospy.Publisher("instrument_tests", test, queue_size=10)

    while not rospy.is_shutdown():
        if time.time() - imuDataTime >= .1:
            instrument_test.imu = False
        if time.time() - dvlDataTime >= .1:
            instrument_test.dvl = False
        if time.time() - cvDataTime >= .1:
            instrument_test.cv = False
        if time.time() - barDataTime >= .1:
            instrument_test.bar = False
        pub.publish(instrument_test)
        rate.sleep()
        # rospy.spin()



if __name__ == '__main__':
    main()
    # make pub
    # wait for data
    # if vaild return true
    # else false
