import rospy
import time



def imu_callback(data):
    barometer = data
    barDataTime = time.time()
    barData = True
    rospy.loginfo(str(barometer) + ' atm')

def dvl_callback(data):
    barometer = data
    rospy.loginfo(str(barometer) + ' atm')

def cv_callback(data):
    barometer = data
    rospy.loginfo(str(barometer) + ' atm')

def bar_callback(data):
    barometer = data
    rospy.loginfo(str(barometer) + ' atm')




def main():
    rospy.init_node('tester', anonymous=True)
    sub = rospy.Subscriber("imu_data", Int16, callback)
    sub = rospy.Subscriber("cv_data", Int16, callback)
    sub = rospy.Subscriber("bar_data", Int16, callback)
    sub = rospy.Subscriber("dvl_data", Int16, callback)
    pub = rospy.Publisher("instrument_tests", test, queue_size=1)

    barData = False
    barDataTime = time.time()

    while True:
        if time.time() - barDataTime >= .01:
            barData = False

        instrument_tests.bar = barData
        pub.publish(instrument_test)

    rospy.spin()



if __name__ == '__main__':
    main()
    # make pub
    # wait for data
    # if vaild return true
    # else false
