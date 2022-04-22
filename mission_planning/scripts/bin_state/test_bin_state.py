#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
from bin_init import add_bin_states
#state imports

#import the states
#import systemcheck from System

def main():
    rospy.init_node('Bin_State_Test_Node')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['complete','failed'])

    # Open the container
    with sm:
        bin_task = smach.StateMachine(outcomes=['success','failed'])
        with bin_task:
            add_bin_states()
        smach.StateMachine.add('bin_task', bin_task, transitions={'success':'complete', 'failed':'failed'})


    # Execute SMACH plan
    outcome = sm.execute()

