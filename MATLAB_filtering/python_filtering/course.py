# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:19:50 2019

@author: Nikita
"""

#importing the required libraries

import matplotlib.pyplot as plt
import numpy as np
from math import pi
import scipy.fftpack as sf
import scipy.signal as sig
from scipy.io import wavfile
from scipy import signal
from scipy.io import loadmat
from numpy.fft import fft
from scipy.signal import firwin, lfilter 
import simpleaudio as sa

plt.close("all")

# Plotting the fft of the original signal

[fs1,y1]=wavfile.read(r'C:\Users\Nikita\Downloads\SYB35.wav')
ts=1/fs1
p=len(y1)
t=[i*ts for i in range (p)]
k=[i*fs1/p for i in range (p)]
x1=fft(y1)

plt.plot(k,abs(fft(y1)))
plt.title(" FFT of Original signal")
plt.xlabel("frequency")
plt.ylabel("amplitude")
plt.show()

#plotting the fft of the noisy signal

[fs2,y2]=wavfile.read(r'C:\Users\Nikita\Downloads\noisy35.wav')
x2=fft(y2)

plt.plot(k,abs(fft(y2)))
plt.title("FFT of Noisy signal")
plt.xlabel("frequency")
plt.ylabel("amplitude")
plt.show()

#loading the .mat file
noisy = loadmat(r'C:\Users\Nikita\Downloads\noisy35.mat')
x3 = []
for i in noisy['x3']: 
    x3.extend(i)

#filtering of the signal
nyq = fs2//2
norm_cutoff = 1000/nyq
fil=signal.firwin(1000,norm_cutoff)
filt = signal.lfilter(fil,1,x3)

plt.plot(t,filt)
plt.title("Filtered signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()

plt.plot(k,abs(fft(filt)))
plt.title("FFT of filtered signal")
plt.xlabel("frequency")
plt.ylabel("amplitude")
plt.show()

#playing the original signal
wave_obj = sa.WaveObject.from_wave_file(r'C:\Users\Nikita\Downloads\SYB35.wav')
play_obj = wave_obj.play()
play_obj.wait_done() # wait for playback to finish before exiting

#playing the noisy signal
wave_obj = sa.WaveObject.from_wave_file(r'C:\Users\Nikita\Downloads\noisy35.wav')
play_obj = wave_obj.play()
play_obj.wait_done() # wait for playback to finish before exiting

filt *= 32767 / np.max(np.abs(filt))

# convert to 16-bit data
filt = filt.astype(np.int16)
# start playback
play_obj = sa.play_buffer(filt, 1, 2, fs2)
play_obj.wait_done()






