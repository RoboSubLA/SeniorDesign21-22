#! /usr/bin/env python
import rosbag
import rospy
#from std_msgs.msg import Int32, String
from ez_async_data.msg import Rotation


def callback(data):
    rospy.loginfo("Yaw: %d, Pitch: %d, Roll: %d" % (data.yaw, data.pitch, data.roll))
    
def listener():
    rospy.init_node('custom_listener', anonymous=True)
    rospy.Subscriber("current_rotation", Rotation, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()