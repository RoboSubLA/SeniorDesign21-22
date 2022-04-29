#!/usr/bin/env python

import smach
import smach_ros

from utilities.lost_target import LostTarget
from utilities.reattempt import Reattempt
from dropper_position_sub import PositionSub
from execute_dropper import add_ex_dropper_states

def add_dropper_states():

    smach.StateMachine.add('position_sub', PositionSub(), transitions={'success':'execute_dropper', 'failed':'failed', 'timeout':'reset_for_reattempt'})

##add sub state machine
    ex_dropper = smach.StateMachine(outcomes=['success', 'reset_for_reattempt'])
    with ex_dropper:
        add_ex_dropper_states()
    smach.StateMachine.add('execute_dropper', ex_dropper, transitions={'success':'success', 'reset_for_reattempt':'reset_for_reattempt'})
    ##

    smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'failed'})
    smach.StateMachine.add('reset_for_reattempt', Reattempt(), transitions={'complete':'position_sub', 'lost_target':'lost_target'})
