import smach

class LostTarget(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['found','timeout'])
    
    def execute(self, userdata):
        pass