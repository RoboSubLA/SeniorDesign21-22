where are we in relation to the gate?
	CV distance? angle
	angle will be sub in relation to gate, positive means to the right of the 		object, negative to the left of the object
	transitions
		move to align if target in sight but not aligned
		execute if target in sight and aligned
		lost target if object lost from sight

move
	strafe in opp dir of error (if +right move left)(if -left move right)
	acceleration varies dependeing on error
	send to controls "strafe direction accel"
	depth correction
	wait .10 seconds (time can be changed)
	go back to where are we

execute

move forward with vision
	while check for gate is true
		check angle
		if angle not in correct range
			strafe in direction
			send to controls "strafe_direction .25"
		send to controls "forward 1"
	else
		move forawrd no vision

move forward no vision
	for 20 seconds
		send to controls "forward 1"