# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 2
# Problem 4

import numpy as np

#Adaptive Trapezoidal Rule Method

#Define Function
def f(x):
    return (np.sin(np.sqrt(100*x)))**2

#Establish Range of integration  
a = 0.
b = 1.

#Choose an initial number of Steps N1 and decide target accuracy for the
#value of the integral.
N1 = 1
h = (b-a)/N1
error = 0.

#Calculate the first approximation I1 to the integral using the chosen
#value N1 with the standard trapezoidal rule formula (Eq. 5.3).
I1 = (0.5*f(a) + 0.5*f(b))*h

#Display Results
print "Slices: ", N1, "   Integral:", I1,"   Error: ", error

Ii = I1
Ni = 2*N1
I = 0.5*Ii
error = 1

#Double the number of steps and use Eq. 5.34 to calculate an improved 
#estimate of the integral. Also calculate the error on that estimate 
#from Eq. 5.30. If the absolute magnitude of the error is less than the
#target accuracy for the integral, stop. Otherwise repeat above.

while( error > 10**(-6) ):
    hi = (b-a)/Ni
    
    for n in range(1,Ni-1,2):
        I += (f(n*hi))*hi
        
    error = (1/3.)*(abs(I-Ii))
    print "Slices: ", Ni, "   Integral:", I,"   Error: ", error
    Ii = I
    I = 0.5*I
    Ni = 2*Ni
