#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
from torpedo_init import add_torpedo_states
#state imports

#import the states
#import systemcheck from System

def main():
    rospy.init_node('Torpedo_State_Test_Node')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['complete','failed'])

    # Open the container
    with sm:
        torpedo_task = smach.StateMachine(outcomes=['success','failed'])
        with torpedo_task:
            add_torpedo_states()
        smach.StateMachine.add('torpedo_task', torpedo_task, transitions={'success':'complete', 'failed':'failed'})


    # Execute SMACH plan
    outcome = sm.execute()

