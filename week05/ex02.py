# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 5
# Problem 2

# -----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Write a program to calculate the coefficients in the discrete Fourier 
# transforms of the following periodic functions sampled at N = 1000 evenly
# spaced points, and make plots of their amplitudes (similar to Figure 7.4
# in the book):

#------------------------------------------------------------------------------

# Part A: A single cycle of a square-wave with amplitude 1

def dft(y):
    
    N = len(y)
    value = np.zeros(N//2+1, complex)
    
    for n in range(N//2+1):
        
        for k in range(N):
            value[n] += y[k]*np.exp(-2j*np.pi*n*k/N)
            
    return value

x = np.linspace(0., 1., 20)
y = signal.square(x)
y -= np.sum(x) / float(len(x))
co = dft(y)

plt.figure(1)
plt.plot(np.arange(len(co)),np.abs(co)**2, linewidth = 3, color= "black")
plt.title("Amplitude of Square-Wave")
plt.xlabel("k (proportional to frequency)")
plt.ylabel("Amplitude")
plt.savefig('Amplitude_Square_Wave')

# -----------------------------------------------------------------------------

# PART B: The sawtooth wave yn = n

x = np.linspace(0., 1., 20)
y = x
y -= (np.sum(x) / float(len(x)))
co = dft(y)

plt.figure(2)
plt.xlim([0, 3])
plt.gca().invert_xaxis()
plt.plot(np.arange(len(co)), np.abs(co)**2, linewidth = 3, color= "black")
plt.title("Amplitude of Sawtooth Wave")
plt.xlabel("k (proportional to frequency)")
plt.ylabel("Amplitude")
plt.savefig('Amplitude_Sawtooth')

# -----------------------------------------------------------------------------

# Part C: The modulated sine wave yn = sin(pi*n/N) * sin(20*pi*n/N) 
    
x = np.linspace(0., 1., 1000)
y = []

for n in range(len(x)):
    y.append(np.sin(np.pi*x[n]) * np.sin(20.*np.pi*x[n]))      
y -= (np.sum(x) / float(len(x)))

plt.figure(3)
co = dft(y)
plt.plot(np.arange(len(co)), np.abs(co)**2, linewidth = 3, color = "black")
plt.title("Amplitude of Sin(pi*n/N) * Sin(20*pi*n/N)")
plt.xlabel("k (proportional to frequency)")
plt.ylabel("Amplitude")
plt.savefig('Amplitude_Sin')

# -----------------------------------------------------------------------------