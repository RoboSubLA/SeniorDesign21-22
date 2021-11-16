#!/usr/bin/env python

import smach
import smach_ros

from utilities.lost_target import LostTarget
from utilities.reattempt import Reattempt
from buoy_position_sub import PositionSub
from execute_buoy import add_ex_buoy_states

def add_buoy_states():

    smach.StateMachine.add('position_sub', PositionSub(), transitions={'success':'execute_buoy', 'failed':'failed', 'timeout':'reset_for_reattempt'})

##add sub state machine
    ex_buoy = smach.StateMachine(outcomes=['success', 'reset_for_reattempt'])
    with ex_buoy:
        add_ex_buoy_states()
    smach.StateMachine.add('execute_buoy', ex_buoy, transitions={'success':'success', 'reset_for_reattempt':'reset_for_reattempt'})
    ##

    smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'failed'})
    smach.StateMachine.add('reset_for_reattempt', Reattempt(), transitions={'complete':'position_sub', 'lost_target':'lost_target'})
