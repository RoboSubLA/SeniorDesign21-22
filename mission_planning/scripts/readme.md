# Notes on adding and removing states using the state_machine_init.py

#### all states in the init file will either be in the form of a state class
class Foo(smach.State)

#### added to the state machine using the following
smach.StateMachine.add('foo', Foo(), transitions{'outcome':'next_state'})

### or as a function import of a state machine declaration (attaching a sub state machine to the upper level one)

##### define the new sub-statemachine
foo = smach.stateMachine(outcomes=['outcome1','outcome2', etc])

#### add all substates to the state machine using defined function
with foo_machine:
    add_all_foo_substates()

#### add the new state machine as a substate

smach.StateMachine.add('foo', foo, transitions{'outcome':'next_state'})

