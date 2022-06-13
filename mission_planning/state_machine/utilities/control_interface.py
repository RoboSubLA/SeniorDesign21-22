#! /usr/bin/env python
import rospy
from robosub_messages.msg import ControlSetpoints, SensorInfo
from subscriber import Subscriber

class ControlInterface(object):
    def __init__(self) -> None:
        self.setpoints_publisher = rospy.Publisher("control_setpoints", ControlSetpoints, queue_size=1)
        self.barometer_subscriber = Subscriber('barometer_topic')
        self.sonar_subscriber = Subscriber('sonar_topic')
        self.imu_subscriber = Subscriber('imu_topic')
        self.dvl_subscriber = Subscriber('dvl_topic')
        self.hydrophones_subscriber = Subscriber('hydrophones_topic')

    def getCurrentData(self):
        setpoints = ControlSetpoints()
        setpoints.depth_setpoint = self.barometer_subscriber.get_data().depth
        setpoints.yaw_setpoint = self.imu_subscriber.get_data().yaw
        setpoints.roll_setpoint = self.imu_subscriber.get_data().roll
        setpoints.pitch_setpoint = self.imu_subscriber.get_data().pitch

        return setpoints

    def publish(self, setpoints):
        self.setpoints_publisher.publish(setpoints)

    def setYaw(self, yaw):
        setpoints = getCurrentData()
        setpoints.yaw_setpoint = yaw
        self.publish(setpoints)

    def setRoll(self, roll):
        setpoints = getCurrentData()
        setpoints.roll_setpoint = roll
        self.publish(setpoints)

    def setPitch(self, pitch):
        setpoints = getCurrentData()
        setpoints.pitch_setpoint = pitch
        self.publish(setpoints)

    def setDepth(self, depth):
        setpoints = getCurrentData()
        setpoints.depth_setpoint = depth
        self.publish(setpoints)

    # TO DO
    def setStrafe(self, strafe):
        setpoints = getCurrentData()
        self.publish(setpoints)
        pass

    def setForward(self, forward):
        setpoints = getCurrentData()
        self.publish(setpoints)
        pass

    def setYawStrafe(self, yaw, strafe):
        setpoints = getCurrentData()

        self.publish(setpoints)
        pass
