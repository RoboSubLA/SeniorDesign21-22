#!/usr/bin/env python

import smach
import smach_ros

from utilities.lost_target import LostTarget
from utilities.reattempt import Reattempt
from lost_target import LostTarget
from reset_for_reattempt import ResetForReattempt
from position_sub import PositionSub
from execute_gate import add_ex_gate_states
from execute_gate import MoveForwardVision
from execute_gate import MoveForwardNoVision

# gate_init.py will add all the necessary gate states to the state machine.
def add_gate_states():
	# Adding the first state that comes after state_zero is passed, the position_sub state, in which the AUV aligns itself with the gate, so that it may pass
	# through the gate without any trouble.
	
    # position_sub = smach.StateMachine(outcomes=['success','timeout','no_target'])
	
	# with position_sub:
    #     add_position_sub_states()
		
    smach.StateMachine.add('reset_for_reattempt', ResetForReattempt(), transitions={'complete':'position_sub'})
    smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'failed'})
    smach.StateMachine.add('position_sub', PositionSub(), transitions={'success':'move_forward_vision', 'timeout':'reset_for_reattempt', 'no_target':'lost_target'})

	# Adding the execute gate (ex_gate) states, which will tell the AUV to begin moving towards the gate.
    smach.StateMachine.add('move_forward_vision', MoveForwardVision(), transitions={'success':'move_forward_no_vision', 'failed':'reset_for_reattempt'})
    smach.StateMachine.add('move_forward_no_vision', MoveForwardNoVision(), transitions={'success':'success', 'failed':'reset_for_reattempt'})
