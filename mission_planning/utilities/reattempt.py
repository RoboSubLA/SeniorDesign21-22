import smach

#tasked with returning the AUV to the initial approach waypoiny and direction

class Reattempt(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','failed'])
    
    def execute(self, userdata):
        pass