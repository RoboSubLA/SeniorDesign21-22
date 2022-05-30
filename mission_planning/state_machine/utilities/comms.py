import rospy
# from pub_state_test.msg import cv_data
import threading

# from std_msgs.msg import String
# type_list = {'string':String}

class Subscriber():
    def __init__(self, topic, data_type):
        self.mutex = threading.Lock()
        self.object_data = rospy.Subscriber(topic, data_type, self.callback)

        self.data = data_type()

    def callback(self, data):
        self.mutex.acquire()
        self.data = data
        self.mutex.release()

    def get_data(self):
        self.mutex.acquire()
        output = self.data
        self.mutex.release()
        return 