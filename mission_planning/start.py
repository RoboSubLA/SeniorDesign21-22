#!/usr/bin/env python
import sys

# Avoid naming files and folders the same name
# It may cause an import error
# to run: rosrun mission_planning start.py 'state you want to run' in catkin_ws

def start_state_machine():
    from scripts.state_machine_init import main
    main()

def start_zero_state_machine():
    from scripts.state_zero.state_zero import main
    main()

def start_gate_state_machine():
    from scripts.gate_state.test_gate_state import main
    main()

if __name__=='__main__':
    # print(abspath(getsourcefile(lambda:0)))
    for arg in sys.argv:
        print(arg)
    if len(sys.argv) < 2:
        # print('Incorrect Number of Arguments')
        # return 0
        sys.exit("Incorrect Number of Arguments\nenter desired entry point as argument")
    
    startPoints = {'start': start_state_machine,
                   'gate': start_gate_state_machine,
		   'zero': start_zero_state_machine}
    start = sys.argv[1]
    if start not in startPoints:
        print('Start point does not exists, please enter correct start point:')
        for entry in startPoints:
            print('entry')
    else:
        startPoints[start]()
