import smach

#will prpbably need to be passed the imagename that it lost and is trying to reaquire
#example, lost target triggered on the gate

class LostTarget(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['target_found','timeout'])
    
    def execute(self, userdata):
        pass