#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros

#state imports
from state_zero.state_zero import State_Zero
from gate_state.gate_init import add_gate_states

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
        
        #create new sub state machine
        gate_state = smach.StateMachine(outcomes['success','failed'])
        #add all substates to the new sub state machine using declared add_gate_states function
        with gate_state:
            add_gate_states()

    # Execute SMACH plan
    outcome = sm.execute()

if __name__ == '__main__':
    main()

