# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 2
# Problem 1

import numpy as np
import math

print('\n')

print("This program will approximate the integral of a polynomial ")
print("function via both the trapezoidal rule and Simpson's rule. ")

print('\n')

print("The user will determine the bounds of this function. ")

def f(x):
    return x**4 - 2.*x + 1.
    
a = input("Enter the lower bound of this function: ")
a = float(a)

b = input("Enter the upper bound of the function: ")
print('\n')
b = float(b)

N = 10

#Trapezoidal Rule
h = (b - a) / float(N)
I = f(a) + f(b)
for k in range(1,N):
	I = I + 2. * f(a + k*h)

I = I * 0.5 * h
print("Trapezoidal Rule Yields: ")
print'I =',I

print('\n')

#Simpson's Rule
k=0.0
x=a + h

for i in range(1, N/2 + 1):
    k += 4 * f(x)
    x += 2 * h

x = a + 2 * h

for i in range(1, N/2):
    k += 2 * f(x)
    x += 2 * h
    
S = (h/3)*(f(a)+f(b)+k)

print("Simpson's Rule Yields: ")
print'I =', S
