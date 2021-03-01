import smach

class PositionSub(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['sub_centered','timeout'])
    
    def execute(self, userdata):
        pass