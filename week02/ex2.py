# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 2
# Problem 2

import numpy as np
import matplotlib.pyplot as plt

print('\n')

# Import velocity.txt and designate time and velocity data
velVStime = np.loadtxt('velocities.txt')
time = velocityVStime[:, 0]
velocity = velVStime[:, 1]

# Calculate Distance
distance = time * velocity
#distance = abs(distance)
np.savetxt('distVStime.txt', zip(time,distance))

# Here I calculated the area under the curve using the trapezoidal rule
# I found the area of each respective trapezoid and summed them

a = 0
N = 100
I = 0
d = abs(distance)
for i in range(1,N):
    h = d[i]
    s1 = time[i] - time[i-1]
    s2 = (d[i-1]-d[i])/(time[i-1]-time[i])
    s = 0.5*(s1+s2)
    I += s*h
print"Trapezoidal Rule Yields: "
print I  
print('\n')

#Simpson's Rule
k = 0.0
h = 1.

for i in range(1, N/2 + 1):
    k += 4 * d[i]
    x += 2 * h

x = a + 2 * h

for i in range(1, N/2):
    k += 2 * d[i]
    x += 2 * h
    
S = (h/3)*(100+k)

print("Simpson's Rule Yields: ")
print S

fig = plt.figure()
up = fig.add_subplot(2,1,1)
up.plot(time,velocity,marker="o",linestyle="-",color="g")
low = fig.add_subplot(2,1,2)
low.plot(time,distance,marker="o",linestyle="-",color="r")

