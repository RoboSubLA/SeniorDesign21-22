#!/usr/bin/env python
import Tkinter as tk
import rospy 
from robosub_messages.msg import Barometer, Sonar, DVL, IMU, Hydrophones
from barometerWidget import BarometerWidget
from sonarWidget import SonarWidget
from dvlWidget import DVLWidget
from imuWidget import IMUWidget
from hydrophonesWidget import HydrophonesWidget

class UserInterface(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

	self.imu = IMU()
	self.imu.roll = 3.2
	self.imu.yaw = 0.8
	self.imu.pitch = 2

	self.sonar = Sonar()
	self.sonar.distance = 10.52
	self.sonar.confidence = 0.8

	self.barometer = Barometer()
	self.barometer.depth = 4
	self.barometer.temperature = 23

	self.dvl = DVL()
	self.dvl.pitch = 3.2
	self.dvl.yaw = 0.8
	self.dvl.roll = 1
	self.dvl.x_translation = 10
	self.dvl.y_translation = 12

	self.hydrophones = Hydrophones()
	self.hydrophones.direction = 170

        #Subscribers
        self.barometer_subscriber =  rospy.Subscriber('barometer_topic', Barometer, self.callback_barometer)
        self.sonar_subscriber = rospy.Subscriber('sonar_topic', Sonar, self.callback_sonar)
        self.dvl_subscriber = rospy.Subscriber('dvl_topic', DVL, self.callback_dvl)
        self.imu_subscriber = rospy.Subscriber('imu_topic', IMU, self.callback_imu)
        self.hydrophones_subscriber = rospy.Subscriber('hydrophones_topic', Hydrophones, self.callback_hydrophones)

	#Publishers
	self.hydrophones_publisher = rospy.Publisher('hydrophones_topic', Hydrophones, queue_size=10)
	self.imu_publisher = rospy.Publisher('imu_topic', IMU, queue_size=10)
	self.dvl_publisher = rospy.Publisher('dvl_topic', DVL, queue_size=10)
	self.sonar_publisher = rospy.Publisher('sonar_topic', Sonar, queue_size=10)
	self.barometer_publisher = rospy.Publisher('barometer_topic', Barometer, queue_size=10)


        #Widgets
        self.barometer_widget = BarometerWidget(self)
        self.barometer_widget.pack(side='right', fill='both')

        self.sonar_widget = SonarWidget(self)
        self.sonar_widget.pack(side='right', fill='both')

        self.dvl_widget = DVLWidget(self)
        self.dvl_widget.pack(side='right', fill='both')

        self.imu_widget = IMUWidget(self)
        self.imu_widget.pack(side='right', fill='both')

        self.hydrophones_widget = HydrophonesWidget(self)
        self.hydrophones_widget.pack(side='right', fill='both')

	self.publish_data()

    # Callback functions
    def callback_barometer(self, data):
	self.barometer.depth = data.depth
	self.barometer.temperature = data.temperature

        self.barometer_widget.update(data)

    def callback_sonar(self, data):
	self.sonar.distance = data.distance
	self.sonar.confidence = data.confidence

        self.sonar_widget.update(data)
    
    def callback_dvl(self, data):
	self.dvl.pitch = data.pitch
	self.dvl.yaw = data.yaw
	self.dvl.roll = data.roll
	self.dvl.x_translation = data.x_translation
	self.dvl.y_translation = data.y_translation

        self.dvl_widget.update(data)

    def callback_imu(self, data):
	self.imu.pitch = data.pitch
	self.imu.yaw = data.yaw
	self.imu.roll = data.roll

        self.imu_widget.update(data)

    def callback_hydrophones(self, data):
	self.hydrophones.direction = data.direction
        self.hydrophones_widget.update(data)

    def publish_data(self):
	self.sonar_publisher.publish(self.sonar)
	self.imu_publisher.publish(self.imu)
	self.barometer_publisher.publish(self.barometer)
	self.dvl_publisher.publish(self.dvl)
	self.hydrophones_publisher.publish(self.hydrophones)

	# loops through function after 1 sec
	self.after(1000, self.publish_data)

if __name__ == '__main__':
    rospy.init_node('user_interface', anonymous=True)
    root = tk.Tk()
    root.geometry("1200x400")
    root.title('Robosub User Interface')
    user_interface = UserInterface(root)
    user_interface.pack()
    user_interface.mainloop()
