#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros

from gate_state.gate_state import Gate_State

def main():
    rospy.init_node('state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['failed','complete'])

    # Open the container
    with sm:
        smach.StateMachine.add('gate_task', Gate_State() transitions={'success':'buoy_task','failed':'failed'})

    # Execute SMACH plan
    outcome = sm.execute()

if __name__ == '__main__':
    main()
