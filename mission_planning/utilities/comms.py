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
        return output


# class Publisher():
#     def __init__(self, topic, data_type):
#         self.pub = rospy.Publisher(topic, type_list[data_type], queue_size=1)
#         pub_type = {'cv_data': self.cv_data_pub}
#         # self.data = pub_type[data_type]()
#         self.publish = pub_type[data_type]
#         self.data = type_list[data_type]()

#     def cv_data_pub(self, gate=None, dice=None):
#         self.data.gate = gate
#         self.data.dice= dice
#         self.pub.publish(self.data)