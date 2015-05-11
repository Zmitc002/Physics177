# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 5
# Problem 3

# -----------------------------------------------------------------------------

import numpy as np
import matplotlib.pylab as plt

# From the github repository, folder “extra_info_labs” please download the file
# “sunspots.txt” which contains the observed number of sunspots on the Sun for
# each month since January 1749. The file contains two columns of numbers, the
# first representing the month and the second being the sunspot number. 

# -----------------------------------------------------------------------------

# Part A: Make a graph of the sunspots as a function of time. You should see
# that the number of sunspots has fluctuated on a regular cycle for as long as
# observations have been recorded. Make an estimate of the length of the cycle
# in months. 

def sunspots(y):
    
    N = len(y)
    value = np.zeros(N//2+1, complex)
    
    for n in range(N//2+1):
        
        for k in range(N):
            value[n] += y[k]*np.exp(-2j*np.pi*n*k / N)
            
    return value
    
sunData = np.loadtxt('sunspots.txt')
time = sunData[:, 0]
spotnumber = sunData[:, 1]

plt.figure(1)
plt.plot(time,spotnumber, color = "black")
plt.title("Sunspots")
plt.xlabel('Months')
plt.ylabel('Spot Frequency')
plt.savefig('Sunspot_Frequency')

# -----------------------------------------------------------------------------

# Part B: Write a program to calculate the Fourier transform of the sunspot 
# data and then make a graph of the magnitude squared |ck|2 of the Fourier 
# as a function of k —also called the power spectrum of the sunspot signal.
# You should see that there is a noticeable peak in the power spectrum at a
# nonzero value of k. The appearance of this peak tells us that there is one 

spotnumber -= (np.sum(time) / float(len(time)))
time = np.linspace(0.,1.,20)
co = sunspots(spotnumber)

plt.figure(2)
plt.xlim([0, 100])
plt.plot(np.arange(len(co)), np.abs(co)**2, linewidth = 3, color = "black")
plt.title("Sunspot Coefficients")
plt.xlabel('k (proportional to frequency)')
plt.ylabel('Amplitude')
plt.savefig('Sunspot_Coefficients')

# -----------------------------------------------------------------------------

# Part C: Find the approximate value of k to which the peak corresponds. 
# What is the period of the sine wave with this value of k? You should find 
# that the period corresponds roughly to the length of the cycle that you 
# estimated in part A.

print("The two first peaks appear to occur near k values 0 and 25.")
print("The respective periods appear to be 0 and 0.013 s.")

# -----------------------------------------------------------------------------