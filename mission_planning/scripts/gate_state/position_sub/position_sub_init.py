#!/usr/bin/env python

import smach
import smach_ros

from current_location import CurrentLocation
from move_to_align import MoveToAlign
from lost_target import LostTarget

def add_position_sub_states():
    #where are we
    smach.StateMachine.add('current_location', CurrentLocation(), transitions={'not_centered':'move_to_align', 'sub_centered':'execute_gate', 'lost_target':'lost_target'})
    #move to align
    smach.StateMachine.add('move_to_align', MoveToAlign(), transitions={'success':'current_location'})
    #lost_target
    smach.StateMachine.add('lost_target', LostTarget(), transitions={'target_found':'position_sub', 'timeout':'failed'})
