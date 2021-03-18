import smach

#tasked with returning the AUV to the initial approach waypoiny and direction

class Reattempt(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['complete','lost_target'])
    
    def execute(self, userdata):
        pass