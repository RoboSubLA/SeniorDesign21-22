#! /usr/bin/env python
import rospy
from robosub_messages.msg import ControlSetpoints, SensorInfo, Action
from subscriber import Subscriber

class ControlInterface(object):
    def __init__(self) -> None:
        self.action_publisher = rospy.Publisher('desired_action', Action, queue_size=10)
        self.setpoints_publisher = rospy.Publisher("control_setpoints", ControlSetpoints, queue_size=1)
        self.barometer_subscriber = Subscriber('barometer_topic')
        self.sonar_subscriber = Subscriber('sonar_topic')
        self.imu_subscriber = Subscriber('imu_topic')
        self.dvl_subscriber = Subscriber('dvl_topic')
        self.hydrophones_subscriber = Subscriber('hydrophones_topic')
        self.robosub_status_subscriber = Subscriber('robosub_status')


    def getCurrentData(self):
        setpoints = ControlSetpoints()
        setpoints.depth_setpoint = self.barometer_subscriber.get_data().depth
        setpoints.yaw_setpoint = self.imu_subscriber.get_data().yaw
        setpoints.roll_setpoint = self.imu_subscriber.get_data().roll
        setpoints.pitch_setpoint = self.imu_subscriber.get_data().pitch

        return setpoints

    def publish(self, setpoints):
        self.setpoints_publisher.publish(setpoints)

    def isInstrumentsConnected(self):
        counter = 0
        while counter < 5000:
            all_active = True
            if not imu_subscriber.is_active():
                all_active = False
            elif not barometer_subscriber.is_active():
                all_active = False
            elif not sonar_subscriber.is_active():
                all_active = False
            elif not hydrophones_subscriber.is_active():
                all_active = False
            elif not dvl_subscriber.is_active():
                all_active = False

            if all_active:
                return True

        return False

    def isStabilized(self):
        if robosub_status_subscriber.get_data().isStabilized:
            return True

        return False

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

    def setDistance(self, distance):
        setpoints = getCurrentData()
        setpoints.distance_setpoint = distance
        self.publish(setpoints)

    def bumpIntoBuoy(self):
        action = Action()
        action.bumpIntoBuoy = True
        self.action_publisher.publish(action)

    # TO DO
    def setStrafe(self, strafe):
        setpoints = getCurrentData()
        self.publish(setpoints)
        pass


    def centerCVObject(self, object):
        pass


    def setYawStrafe(self, yaw, strafe):
        setpoints = getCurrentData()

        self.publish(setpoints)
        pass
