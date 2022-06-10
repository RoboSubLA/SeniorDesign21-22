import smach
import rospy
from utilities.reset_for_reattempt import ResetForReattempt
from utilities.lost_target import LostTarget
from utilities.subscriber import Subscriber
from robosub_messages.msg import CV

# State machine for the gate task.
class GateTask(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, outcomes=['success','failed'])
        with self:
            smach.StateMachine.add('align_with_gate', AlignWithGate(), transitions={'success': 'move_forward_vision', 'failed': 'reset_for_reattempt'})
            smach.StateMachine.add('move_forward_vision', MoveForwardVision(), transitions={'success':'move_forward_no_vision', 'failed':'reset_for_reattempt'})
            smach.StateMachine.add('move_forward_no_vision', MoveForwardNoVision(), transitions={'success':'success', 'failed':'reset_for_reattempt'})
            smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'align_with_gate', 'timeout':'failed'})
            smach.StateMachine.add('reset_for_reattempt', ResetForReattempt(), transitions={'complete':'align_with_gate', 'lost_target':'lost_target'})
      
# Add different sub states under here.
class AlignWithGate(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','failed'])
        self.aligned = False
        self.cv_subscriber = Subscriber('cv_topic') #Array with objects. Object form: object, xoffset, yoffset, distance
        self.cv_data = cv_subscriber.get_data()
        self.is_centered = False

    def execute(self, userdata):
        # Center Sub
        while self.cv_data:
            #centerObject(cv_data)
            if(abs(self.cv_data.xoffset) < 5 and abs(self.cv_data.yoffset) < 5):
                print('Is centered')
                self.is_centered = True
            else:
                self.is_centered = False

        transition = 1
        if transition == 1:
            rospy.loginfo("success")
            return 'success'
        else:
            rospy.loginfo("failed")
            return 'failed'
    def center(self):

class MoveForwardVision(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','failed'])

    def execute(self, userdata):
        #Move forward while cv object x and y is center of frame.
        return 'success'
        

class MoveForwardNoVision(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','failed'])

    def execute(self, userdata):
       #Move forward
       return 'success'

