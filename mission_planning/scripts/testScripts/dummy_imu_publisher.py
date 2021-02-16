#!/usr/bin/env python
import rospy
from ez_async_data.msg import Rotation
import time
# from std_msgs.msg import Float32

class DummyIMU:
    def __init__(self):
        self.pitch = 0
        self.pitch_direction = 1

        self.yaw = 0
        self.yaw_direction = 1

        self.roll = 0
        self.roll_direction = 1

    def changePitch(self):
        if self.pitch_direction == 1:
            self.pitch = self.pitch + self.pitch_direction
            if self.pitch >= 20:
                self.pitch = 20
                self.pitch_direction = -1
        else:
            self.pitch = self.pitch + self.pitch_direction
            if self.pitch <= -20:
                self.pitch = -20
                self.pitch_direction = 1

    def changeYaw(self):
        if self.yaw_direction == 1:
            self.yaw = self.yaw + self.yaw_direction
            if self.yaw >= 35:
                self.yaw = 35
                self.yaw_direction = -1
        else:
            self.yaw = self.yaw + self.yaw_direction
            if self.yaw <= -35:
                self.yaw = -35
                self.yaw_direction = 1

    def changeRoll(self):
        if self.roll_direction == 1:
            self.roll = self.roll + self.roll_direction
            if self.roll >= 15:
                self.roll = 15
                self.roll_direction = -1
        else:
            self.roll = self.roll + self.roll_direction
            if self.roll <= -15:
                self.roll = -15
                self.roll_direction = 1

    def getMsg(self):
        output = Rotation()
        output.pitch = self.pitch
        output.yaw = self.yaw
        output.roll = self.roll
        return output

def talker():
    pub = rospy.Publisher('current_rotation', Rotation, queue_size=0)
    # pubRoll = rospy.Publisher('roll', Float32, queue_size=0)
    # pubPitch = rospy.Publisher('pitch', Float32, queue_size=0)
    # pubYaw = rospy.Publisher('yaw', Float32, queue_size=0)

    rospy.init_node('dummy_imu_pub', anonymous=True)
    r = rospy.Rate(30) 
    
    msg = Rotation()

    # msgRoll = Float32()
    # msgPitch = Float32()
    # msgYaw = Float32()
    imu = DummyIMU()
    start_time = time.time()
    while not rospy.is_shutdown():
        
        # msg.pitch = 0
        # msg.roll = 0
        # msg.yaw = 50
        elapsedTime = time.time() - start_time
        # rospy.loginfo(elapsedTime)
        if (elapsedTime)>.01:
            start_time = time.time()
            imu.changePitch()
            imu.changeRoll()
            imu.changeYaw()

            # msg = imu.getMsg()
            msg.pitch = imu.pitch
            msg.yaw = imu.yaw
            msg.roll = imu.roll

        rospy.loginfo(msg)
        pub.publish(msg)
        
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: 
        pass
