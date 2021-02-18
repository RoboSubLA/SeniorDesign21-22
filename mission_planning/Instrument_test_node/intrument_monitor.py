import rospy
import time
from ez_async_data.msg import Barometer
from ez_async_data.msg import Rotation

def imu_callback(data):
    barDataTime = time.time()
    barData = True
    rospy.loginfo("Pitch: %d, Yaw: %d, Roll: %d", data.pitch, data.yaw, data.roll)

def dvl_callback(data):
    rospy.loginfo(str(barometer) + ' atm')

def cv_callback(data):
    rospy.loginfo(str(barometer) + ' atm')

def bar_callback(data):
    # barometer data should register the average atm of a standard swimming pool (~700 - 770)
    rospy.loginfo('Barometer: ' + str(data.atm) + ' atm')
    print()




def main():
    rospy.init_node('tester', anonymous=True)
    rospy.Subscriber("imu_data", Rotation, imu_callback)
    # rospy.Subscriber("cv_data", Int16, cv_callback)
    rospy.Subscriber("bar_data", Barometer, bar_callback)
    # rospy.Subscriber("dvl_data", Int16, dvl_callback)
    # pub = rospy.Publisher("instrument_tests", test, queue_size=1)
    
    barData = False
    barDataTime = time.time()

    while True:
        if time.time() - barDataTime >= .01:
            barData = False

        # instrument_tests.bar = barData
        # pub.publish(instrument_test)

    rospy.spin()



if __name__ == '__main__':
    main()
    # make pub
    # wait for data
    # if vaild return true
    # else false
