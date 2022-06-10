#!/usr/bin/env python
import rospy
import smach
import smach_ros
from state_zero.state_zero import StateZero
from gate_task.gate_task import GateTask
from buoy_task.buoy_task import BuoyTask
from bin_task.bin_task import BinTask
from torpedo_task.torpedo_task import TorpedoTask
from octagon_task.octagon_task import OctagonTask
from path_marker.path_marker import PathMarker
from locate_ping.locate_ping import LocatePing

def main():
    rospy.init_node('state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['failed','complete'])
    sm.userdata.team = 'bootlegger' #options 'bootlegger' or 'gman'

    # Open the container
    with sm:
        smach.StateMachine.add('system_check', StateZero(), transitions={'passed':'gate_task', 'failed':'failed'})
        smach.StateMachine.add('gate_task', GateTask(), transitions={'success':'path_marker','failed':'failed'})
        smach.StateMachine.add('buoy_task', BuoyTask(), transitions={'success': 'bin_task', 'failed': 'failed'})
        smach.StateMachine.add('bin_task', BinTask(), transitions={'success': 'torpedo_task', 'failed': 'failed'})
        smach.StateMachine.add('torpedo_task', TorpedoTask(), transitions={'success': 'complete', 'failed': 'failed'})
        smach.StateMachine.add('octagon_task', OctagonTask(), transitions={'success': 'complete', 'failed': 'failed'})
        smach.StateMachine.add('path_marker', PathMarker(), transitions={'buoy': 'buoy_task', 'bin': 'bin_task', 'failed': 'failed'})
        smach.StateMachine.add('locate_ping', LocatePing(), transitions={'torpedo': 'torpedo_task', 'octagon': 'octagon_task', 'failed': 'failed'})
    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()
