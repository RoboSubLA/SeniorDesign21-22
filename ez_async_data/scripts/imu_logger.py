#! /usr/bin/env python
import rosbag
import rospy
#from std_msgs.msg import Int32, String
from ez_async_data.msg import Rotation

#makes the file to write data
from os.path import expanduser
home = expanduser("~")

bag = None


def callback(data):
    rospy.loginfo("Yaw: %d, Pitch: %d, Roll: %d" % (data.yaw, data.pitch, data.roll))
    try:
        bag.write('imu', data)
    finally:
        bag.close()
    
    
def listener():
    rospy.init_node('custom_listener', anonymous=True)
    rospy.Subscriber("current_rotation", Rotation, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    bag = rosbag.Bag(home+'/catkin/src/ez_async_data/bagfiles/imu_data.bag', 'w')
    listener()

    

#try:
    #s = String()
    #s.data = 'foo'

    #i = Int32()
    #i.data = 42

    #bag.write('chatter', s)
    #bag.write('numbers', i)
#finally:
    #bag.close()
