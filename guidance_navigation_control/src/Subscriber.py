import rospy
import threading
from robosub_messages.msg import Action
from robosub_messages.msg import ControlCommand
from robosub_messages.msg import Barometer, DVL, IMU, Sonar, Hydrophones

topic_to_datatype = {
    'barometer_topic': Barometer,
    'dvl_topic': DVL, 
    'imu_topic': IMU,
    'sonar_topic': Sonar,
    'hydrophones_topic': Hydrophones,
	'action': Action, 
    'controlCommand': ControlCommand
    }

class Subscribe_to():
	def __init__(self, topic):
		self.mutex = threading.Lock()
		self.foo = rospy.Subscriber(topic, topic_to_datatype[topic], self.callback)
		self.data = topic_to_datatype[topic]()
		self.new_data = False

	def callback(self, cb_data):	#Gets data from publisher
		self.mutex.acquire()
		self.data = cb_data
		self.new_data = True
		self.mutex.release()

	def get_data(self):		#Gives you the most recent data got
		self.mutex.acquire()
		self.final_data = self.data
		self.new_data = False
		self.mutex.release()
		return self.final_data

	def was_data_sent(self):	#Tells you if new data was acquired yet
		self.mutex.acquire()
		self.check = self.new_data
		self.mutex.release()
		return self.