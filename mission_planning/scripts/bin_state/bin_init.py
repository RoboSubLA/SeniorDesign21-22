#!/usr/bin/env python

import smach
import smach_ros

from utilities.lost_target import LostTarget
from utilities.reattempt import Reattempt
from bin_position_sub import PositionSub
from execute_bin import add_ex_bin_states

def add_bin_states():

    smach.StateMachine.add('position_sub', PositionSub(), transitions={'success':'execute_bin', 'failed':'failed', 'timeout':'reset_for_reattempt'})

##add sub state machine
    ex_bin = smach.StateMachine(outcomes=['success', 'reset_for_reattempt'])
    with ex_bin:
        add_ex_bin_states()
    smach.StateMachine.add('execute_bin', ex_bin, transitions={'success':'success', 'reset_for_reattempt':'reset_for_reattempt'})
    ##

    smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'failed'})
    smach.StateMachine.add('reset_for_reattempt', Reattempt(), transitions={'complete':'position_sub', 'lost_target':'lost_target'})
