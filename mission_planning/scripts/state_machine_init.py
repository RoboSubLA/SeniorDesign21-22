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
                               transitions={'passed':'gate_task', 'failed':'failed'})
        
        ##declaration of new sub state machine###
        #create new sub state machine
        gate_task = smach.StateMachine(outcomes=['success','failed'])
        #add all substates to the new sub state machine using declared add_gate_states function
        with gate_task:
            add_gate_states()
        #add the new substate machine to the previous one (sm), add in the approproate transitions to new states
        smach.StateMachine.add('gate_task', gate_task, transitions={'success':'complete', 			'failed':'failed'})
        #note that when adding a substatemachine there is no brackets, unlike the state zero in which we call the state constructor
        ###end declaration of new sub state machine####

    # Execute SMACH plan
    outcome = sm.execute()

if __name__ == '__main__':
    main()
