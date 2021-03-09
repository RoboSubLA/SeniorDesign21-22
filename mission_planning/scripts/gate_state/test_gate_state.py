#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
from gate_init import add_gate_states
#state imports

#import the states
#import systemcheck from System

def main():
    rospy.init_node('Gate_State_Test_Node')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['failed','complete'])

    # Open the container
    with sm:
        gate_task = smach.StateMachine(outcomes=['success','failed'])
        with gate_task:
            add_gate_states()
        smach.StateMachine.add('gate_task', gate_task, transitions={'success':'complete', 'failed':'failed'})


    # Execute SMACH plan
    outcome = sm.execute()

