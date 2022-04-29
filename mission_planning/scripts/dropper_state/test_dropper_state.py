#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
from dropper_init import add_dropper_states
#state imports

#import the states
#import systemcheck from System

def main():
    rospy.init_node('Dropper_State_Test_Node')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['complete','failed'])

    # Open the container
    with sm:
        dropper_task = smach.StateMachine(outcomes=['success','failed'])
        with dropper_task:
            add_dropper_states()
        smach.StateMachine.add('dropper_task', dropper_task, transitions={'success':'complete', 'failed':'failed'})


    # Execute SMACH plan
    outcome = sm.execute()

