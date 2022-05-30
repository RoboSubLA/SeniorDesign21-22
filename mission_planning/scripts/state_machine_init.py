#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros

#state imports
from state_zero.state_zero import State_Zero
from gate_state.gate_init import add_gate_states
from buoy_state.buoy_init import add_buoy_states

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
                               transitions={'passed':'gate_task', 'failed':'failed'})


        #create new sub state machine
        gate_task = smach.StateMachine(outcomes=['success','failed'])
        buoy_task = smach.StateMachine(outcomes=['success','failed'])

        #add all substates to the new sub state machine using declared add_gate_states function
        with gate_task:
            add_gate_states()

        smach.StateMachine.add('gate_task', gate_task, transitions={'success':'buoy_task','failed':'failed'})


        with buoy_task:
            add_buoy_states()

        smach.StateMachine.add('buoy_task', buoy_task, transitions={'success':'complete','failed':'failed'})

    # Execute SMACH plan
    outcome = sm.execute()

if __name__ == '__main__':
    main()
