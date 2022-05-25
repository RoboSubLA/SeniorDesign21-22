#!/usr/bin/env python
import rospy
import smach
import smach_ros
from state_zero.state_zero import StateZero
from gate_task.gate_task import GateTask
from buoy_task.buoy_task import BuoyTask
from bin_task.bin_task import BinTask

def main():
    rospy.init_node('state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['failed','complete'])

    # Open the container
    with sm:
        #smach.StateMachine.add('system_check', StateZero(), transitions={'passed':'gate_task', 'failed':'failed'})
        smach.StateMachine.add('gate_task', GateTask(), transitions={'success':'buoy_task','failed':'failed'})
        smach.StateMachine.add('buoy_task', BuoyTask(), transitions={'success': 'bin_task', 'failed': 'failed'})
        smach.StateMachine.add('bin_task', BinTask(), transitions={'success': 'complete', 'failed': 'failed'})
    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()
