#!/usr/bin/env python

import smach
import smach_ros

from utilities.lost_target import LostTarget
from utilities.reattempt import Reattempt
from torpedo_position_sub import PositionSub
from execute_torpedo import add_ex_torpedo_states

def add_torpedo_states():

    smach.StateMachine.add('position_sub', PositionSub(), transitions={'success':'execute_torpedo', 'failed':'failed', 'timeout':'reset_for_reattempt'})

##add sub state machine
    ex_torpedo = smach.StateMachine(outcomes=['success', 'reset_for_reattempt'])
    with ex_torpedo:
        add_ex_torpedo_states()
    smach.StateMachine.add('execute_torpedo', ex_torpedo, transitions={'success':'success', 'reset_for_reattempt':'reset_for_reattempt'})
    ##

    smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'failed'})
    smach.StateMachine.add('reset_for_reattempt', Reattempt(), transitions={'complete':'position_sub', 'lost_target':'lost_target'})
