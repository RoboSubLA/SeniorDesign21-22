import smach
import rospy
import time

from std_msgs.msg import String
from utilities.comms import Subscriber
from computer_vision.msg import Cv_data

# Takes the data values object and confidence from CV, to find the target that was lost. If the object value matches the lost target, and if the confidence is high enough, for example, 90, 
# then this state will return "target_found". If after some time the target is not found, then return "timeout."

class LostTarget(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['target_found','timeout'])
        self.target = Subscriber('cv_data', Cv_data)
		self.elapsedTime = 0
        self.maxTime = 30
		
    def execute(self, userdata):
		# The targetObject value will be changed as the code for CV is developed. targetObject is basically the object that the AUV is trying to locate. It will most likely be passed by CV.
		targetObject = ''
		beginningTime = time.time()
        
		while(True):
			data = self.target.get_data()
            self.elapsedTime = time.time()
			if (beginningTime - self.elapsedTime) > self.maxTime:
				return('timeout')
			if(data.confidence > 90 and data.object == targetObject):	
				return('target_found')
