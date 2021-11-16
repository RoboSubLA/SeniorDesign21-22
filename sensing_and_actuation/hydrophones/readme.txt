two channels . py, stream data fromt he osciliscope
takes data from two chjannels
makes it usable


right left
two channels
Serial conenction to motherboard

power requirements

power
	each hydro has and amp, and each amp has barrel jack connector
	takes up to 5-12 volts
	

required library 
	picosdk
	https://github.com/picotech/picosdk-python-wrappers

aquarian pa4 preamp
	2 wires going out
	barrel jack 
	bnc conneciton

oscilliscope
	powered through motherboard
	input from the amps
	connects to motherboard using serial connection


pico 2405A
	serial connection
	set up already to get data

connections should not be an issue, straightforward



todo
	set up low and high for quadrent
		need to be able to filter for quadrent
			example b 40khz
			min and max sould be set at range

	butterwoths filter order
		find using website
		https://tools.analog.com/en/filterwizard/
	error mihgt come up if order is too high

	hydraphone array needs to be spaced out 5 times farther


passband set up
	passband to 5 khz

	25
		min
		max
	30
		min
		max
	35
		min
		max
	40
		min
		max
	


errors
	filter order too high
		the numbers created a filter thats not reasonable
		check the min and max

