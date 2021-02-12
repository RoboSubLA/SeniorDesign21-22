#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
from subscriber_state_machine import WaitForTwo


#import the states
#import systemcheck from System


def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['win', 'lose'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('SystemCheck', WaitForTwo(), 
                               transitions={'success':'win', 'failed':'lose'})

    # Execute SMACH plan
    outcome = sm.execute()

if __name__ == '__main__':
    main()

