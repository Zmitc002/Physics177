# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 1
# Problem 3a

print('\n')

import math

h = 800

time = math.sqrt(2*h/9.8)
time = round(time, 2)

print"When dropped the ball will hit the ground in", time, "seconds. "

print('\n')

print"When given an initial velocity other than zero the time of impact "
print"will be equal to [[(vi^2 + 2gh)^(1/2)]-vi]/g where vi is the "
print"initial velocity, g is the gravitational acceleration (9.8 m/s^2), "
print"and h is the height of the tower."

print('\n')


# The only way for this problem to have a "result" is if v is defined.
# Since it is not I assumed that the ball was simply dropped from
# 800 meters. That is, the initial velocity was zero. 