import smach

class CurrentLocation(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','lost_target'])
    
    def execute(self, userdata):
        pass