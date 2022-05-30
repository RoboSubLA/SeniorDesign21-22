import smach

class ResetForReattempt(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['complete', 'lost_target'])
    
    def execute(self, userdata):
        return 'complete'