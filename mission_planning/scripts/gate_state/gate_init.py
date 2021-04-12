#!/usr/bin/env python

import smach
import smach_ros

from utilities.lost_target import LostTarget
from utilities.reattempt import Reattempt
from position_sub import PositionSub
# from mission_planning.scripts.utility_states.reset_for_reattempt import ResetForReattempt
from execute_gate import add_ex_gate_states

def add_gate_states():
    # ##declaration of new sub state machine###
    # #create new sub state machine
    # position_sub = smach.StateMachine(outcomes=['success','failed'])
    # #add all substates to the new sub state machine using declared add_gate_states function
    # with position_sub:
    #     add_position_sub_states()
    # #add the new substate machine to the previous one (sm), add in the approproate transitions to new states
    # smach.StateMachine.add('position_sub', position_sub, transitions={'success':'execute_gate', 'failed':'failed'})
    # #note that when adding a substatemachine there is no brackets, unlike the state zero in which we call the state constructor
    # ###end declaration of new sub state machine####


    smach.StateMachine.add('position_sub', PositionSub(), transitions={'success':'execute_gate', 'failed':'failed', 'timeout':'reset_for_reattempt'})


    ##add sub state machine
    ex_gate = smach.StateMachine(outcomes=['success', 'reset_for_reattempt'])
    with ex_gate:
        add_ex_gate_states()
    smach.StateMachine.add('execute_gate', ex_gate, transitions={'success':'success', 'reset_for_reattempt':'reset_for_reattempt'})
    ##

    smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'failed'})
    smach.StateMachine.add('reset_for_reattempt', Reattempt(), transitions={'complete':'position_sub', 'lost_target':'lost_target'})