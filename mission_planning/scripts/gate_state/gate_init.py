#!/usr/bin/env python

import smach
import smach_ros

from execute_gate import ExecuteGate
from lost_target import LostTarget
from postition_sub import PositionSub
from reset_for_reattempt import ResetForReattempt

def add_gate_states():
    smach.StateMachine.add('position_sub', PositionSub(), transitions={'sub_centered':'execute_gate', 'lost_target':'lost_target'})
    smach.StateMachine.add('execute_gate', ExecuteGate(), transitions={'success':'task_complete', 'failed':'reset_for_reattempt'})
    smach.StateMachine.add('reset_for_reattempt', ResetForReattempt(), transitions={'complete':'position_sub', 'lost_target':'lost_target'})
    smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'task_failed'})
    