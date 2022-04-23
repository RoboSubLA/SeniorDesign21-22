### Connect the right hydrophone to channel A and the left hydrophone to channel B. ### 

import ctypes
import numpy as np
from picosdk.ps2000a import ps2000a as ps
import matplotlib.pyplot as plt
from picosdk.functions import adc2mV, assert_pico_ok
import time
from scipy.signal import butter, lfilter
from scipy.signal import freqz
from scipy.signal import correlate

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

while(1):

	exec(open("Two_Channels.py").read())

	# Filtering variables
	low_cutoff_freq = 18000
	high_cutoff_freq = 52000
	Ts_s = Ts_us / 1000000
	fs = 1.0/Ts_s
	order = 10
	x = 20 * Ts_s

	# Filter raw data
	filtered_signal_A = butter_bandpass_filter(adc2mVChAMax, low_cutoff_freq, high_cutoff_freq, fs, order)
	filtered_signal_B = butter_bandpass_filter(adc2mVChBMax, low_cutoff_freq, high_cutoff_freq, fs, order)

	xcorr = correlate(filtered_signal_A, filtered_signal_B)
	#xcorr_max_index = xcorr.index(max(xcorr))
	xcorr_max_index = np.where(xcorr == (max(xcorr)))
	xcorr_max_index = list(xcorr_max_index) #convert tuple to list
	xcorr_max_index = xcorr_max_index[0] #convert list to np.ndarray
	xcorr_max_index = xcorr_max_index.item(0) #take the first element of the ndarray
	#xcorr_max_index = int(xcorr_max_index) #convert np.ndarray to int ERROR
	#print(xcorr_max_index.item(0))
	#print(type(xcorr_max_index.item(0)))

	sig_length = len(filtered_signal_A)
	lags = list(range((-sig_length+1), sig_length)) #use list() to turn range object into a list
# maybe later dont calculate the lags array and calculate the value of the max xcorr lag directly
	#print(lags[2*(sig_length-1)]) #prints the correct number
	#print(sig_length)
	#print(len(lags))
	#print(2*(sig_length-1))
	#print(type(lags))

	lag_at_max_xcorr = lags[xcorr_max_index]
	time_delay = lag_at_max_xcorr * Ts_s


	
	if (abs(time_delay) <= x): # Threshold the time delay so the sub isnt constantly 
		# changing between left and right
		time_delay = 0



	if (time_delay < 0):
		# right arrived first, left arrived second
		# we want to turn to try to make them equal
		print("Turn right\n")
      
	elif (time_delay > 0):
		# left arrived first, right arrived second
		print("Turn left\n");
	else:
		print("Go straight\n");

