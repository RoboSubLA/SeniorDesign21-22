import smach

#attempts a search pattern toward direction of last known location
#to reaccuire visual on target

#needs to know what object it is looking for as well as last known position

class LostTarget(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['target_found','timeout'])
    
    def execute(self, userdata):
        pass