import time
import rospy

def testFailedTransition(length):
    rospy.loginfo("Waiting for failed result")
    time.sleep(length)
    
    return 'failed'

def testPassedTransition(length):
    rospy.loginfo("Waiting for passed result")
    time.sleep(length)

    return 'passed'