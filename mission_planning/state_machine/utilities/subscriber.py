import rospy
import time
import threading
from robosub_messages.msg import Barometer, Sonar, DVL, IMU, Hydrophones, InstrumentMonitor, CV, ControlSetpoints


topic_datatype = {
    'barometer_topic': Barometer,
    'sonar_topic': Sonar,
    'dvl_topic': DVL,
    'imu_topic': IMU,
    'hydrophones_topic': Hydrophones,
    'instrument_monitor': InstrumentMonitor,
    'cv_topic': CV,
    'control_setpoints': ControlSetpoints
}

class Subscriber():
    def __init__(self, topic):
        self.mutex = threading.Lock()
        self.subscriber = rospy.Subscriber(topic, topic_datatype[topic], self.callback)
        self.data = topic_datatype[topic]
        self.last_updated = 0

    def callback(self, data):
        self.mutex.acquire()
        self.data = data
        self.last_updated = time.time()
        self.mutex.release()

    def get_data(self):
        return self.data

    def is_active(self):
        return time.time() - self.last_updated < .5
