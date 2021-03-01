import smach

class ExecuteGate(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['sucess','failed'])
    
    def execute(self, userdata):
        pass