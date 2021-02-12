#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
from state_zero.state_zero import State_Zero


#import the states
#import systemcheck from System


def main():
    rospy.init_node('Lanturn_State_Machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['failed','complete'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('SystemCheck', State_Zero(), 
                               transitions={'passed':'complete', 'failed':'failed'})

    # Execute SMACH plan
    outcome = sm.execute()

if __name__ == '__main__':
    main()

