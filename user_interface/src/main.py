#!/usr/bin/env python
import Tkinter as tk
import rospy 
from barometer.msg import Barometer 
from sonar.msg import Sonar
from dvl.msg import DVL
from ez_async_data.msg import IMU
from barometerWidget import BarometerWidget
from sonarWidget import SonarWidget
from dvlWidget import DVLWidget
from imuWidget import IMUWidget

class UserInterface(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        #Subscribers
        self.barometer_subscriber =  rospy.Subscriber('barometer_dummy_topic', Barometer, self.callback_barometer)
        self.sonar_subscriber = rospy.Subscriber('sonar_dummy_topic', Sonar, self.callback_sonar)
        self.dvl_subscriber = rospy.Subscriber('dvl_dummy_topic', DVL, self.callback_dvl)
        self.imu_subscriber = rospy.Subscriber('imu_dummy_topic', IMU, self.callback_imu)

        #Widgets
        self.barometer_widget = BarometerWidget(self)
        self.barometer_widget.pack(side='right', fill='both')

        self.sonar_widget = SonarWidget(self)
        self.sonar_widget.pack(side='right', fill='both')

        self.dvl_widget = DVLWidget(self)
        self.dvl_widget.pack(side='right', fill='both')

        self.imu_widget = IMUWidget(self)
        self.imu_widget.pack(side='right', fill='both')

    def callback_barometer(self, data):
        self.barometer_widget.update(str(round(data.depth, 2)))

    def callback_sonar(self, data):
        self.sonar_widget.update(str(round(data.distance, 2)))
    
    def callback_dvl(self, data):
        self.dvl_widget.update(data)

    def callback_imu(self, data):
        self.imu_widget.update(data)

if __name__ == '__main__':
    rospy.init_node('user_interface', anonymous=True)
    root = tk.Tk()
    root.title('Robosub User Interface')
    user_interface = UserInterface(root)
    user_interface.pack()
    user_interface.mainloop()