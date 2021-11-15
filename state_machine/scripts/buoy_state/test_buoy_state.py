#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
from buoy_init import add_buoy_states
#state imports

#import the states
#import systemcheck from System

def main():
    rospy.init_node('Buoy_State_Test_Node')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['complete','failed'])

    # Open the container
    with sm:
        buoy_task = smach.StateMachine(outcomes=['success','failed'])
        with buoy_task:
            add_buoy_states()
        smach.StateMachine.add('buoy_task', buoy_task, transitions={'success':'complete', 'failed':'failed'})


    # Execute SMACH plan
    outcome = sm.execute()

