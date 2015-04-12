# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 1
# Problem 3b

import matplotlib.pyplot as plt
import numpy as np

print('\n')

vmin = input ("Enter the minimum velocity: ")
vmax = input ("Enter the maximum velocity: ")

print('\n')

g = 9.8
h = 800.

velInterval = (vmax-vmin)/10.

v = []
t = []
i = 0
g = 0
w = 0

#This creates a velocity vector with equally spaced velocity components
for i in range(11):
    v.append((i * velInterval) + vmin)
    
v = [round(n,2) for n in v]

#This creates a time vector using equation from part 3a
for w in range(11):
    t.append (((((v[w]**2)+(2*9.8*h))**0.5)-(v[w]))/9.8)
    round(t[w],2)
    
t = [round(n,2) for n in t]
    
plt.plot(v,t,'-o')
plt.xlabel('Velocity [m/s]')
plt.ylabel('Time [s]')

print("Velocity List: ")
print(v)

print('\n')

print("Time List: ")
print(t)

print('\n')

t1 = np.array(t)
np.savetxt('file.dat',t1)

