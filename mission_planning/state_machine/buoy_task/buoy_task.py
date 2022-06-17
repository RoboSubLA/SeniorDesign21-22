import smach
import rospy
from utilities.reset_for_reattempt import ResetForReattempt
from utilities.lost_target import LostTarget

class BuoyTask(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, outcomes=['success','failed'])
        with self:
            smach.StateMachine.add('position_sub', PositionSub(), transitions={'success': 'bump_buoy', 'failed': 'reset_for_reattempt'})
            smach.StateMachine.add('bump_buoy', BumpBuoy(), transitions={'success': 'success', 'failed': 'reset_for_reattempt'})
            smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'failed'})
            smach.StateMachine.add('reset_for_reattempt', ResetForReattempt(), transitions={'complete':'position_sub', 'lost_target':'lost_target'})

class PositionSub(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','failed'])
        self.is_aligned = False
        self.cv_subscriber = Subscriber('cv_topic') #Array with objects. Object form: object, xoffset, yoffset, distance
        self.imu_subscriber = Subscriber('imu_topic')
        self.robosub_status_subscriber = Subscriber('robosub_status')
        self.control_interface = ControlInterface()
        self.counter = 0

    def execute(self, userdata):
        cv_data = cv_subscriber.get_data()

        while cv_data[0].visible:
            cv_data = cv_subscriber.get_data()
            imu_data = imu_subscriber.get_data()
            self.control_interface.centerObject(cv_object.visible)

            if self.is_centered(cv_data[0]):
                self.control_interface.setYaw(0)
                self.control_interface.setDepth(0)

                if control_interface.isStabilized():
                    self.is_aligned = True
                else:
                    self.is_aligned = False

            if self.is_aligned:
                distance_to_buoy = cv_data[0].distance
                self.control_interface.setDistance(distance_to_buoy - 1)

                if distance_to_buoy < 0.1524:
                    self.control_interface.setDistance(0)

                    if self.control_interface.isStabilized():
                        return 'success'
            self.counter += 1

            time.sleep(0.01)
            if self.counter > 6000:
                return 'failed'

        return 'failed'

    def is_centered(self, cv_object):
        if (abs(cv_object.xoffset < 5) and abs(cv_object.yoffset < 5)):
            return True

        return False



class BumpBuoy(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','failed'])
        self.control_interface = ControlInterface()
        self.action_publisher = rospy.Publisher('desired_action', Action, queue_size=10)
        self.counter = 0

    def execute(self, userdata):
        self.control_interface.bumpIntoBuoy()
        while True:
            if self.control_interface.isStabilized():
                return 'success'

            self.counter += 1
            time.sleep(0.01)
            if self.counter > 2000:
                return 'failed'
