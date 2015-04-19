# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 2
# Problem 3

import numpy as np
import scipy as sp


def f(x):
    return x**4 - 2*x + 1
   
N = 20
a = 0.0
b = 2.0

#Trapezoidal Rule
print('\n')
print("The trapezoidal rule applied to the function (x^4)-(2x)+1 yields")

h = (b-a)/N

s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s+= f(a+k*h)
    
print(h*s)

print('\n')
print("Simpson's rule applied to the function (x^4)-(2x)+1 yields")

#Simpson's Rule
k = 0.0
x = a + h
for i in range(1, N/2 + 1):
    k += 4 * f(x)
    x += 2 * h

x = a + 2 * h

for i in range(1, N/2):
    k += 2 * f(x)
    x += 2 * h
    
S = (h/3)*(f(a)+f(b)+k)
print(S)

print('\n')

#Trapezoidal Rule using Numpy Instrinsic Functions
print("Using the numpy instrinsic function, the trapezoidal rule ")
print("applied to the function (x^4)-(2x)+1 yields")

x = np.linspace(a, b, N)
y = f(x)
    
print(np.trapz(y,x,dx=0.1))
print('\n')

#Simpson's Rule using Scipy Instrinsic Functions
print("Using the scipy instrinsic function, Simpson's rule ")
print("applied to the function (x^4)-(2x)+1 yields")

print(sp.integrate.simps(y,x,dx=0.1))

#Practical Estimation Errors: Trapezoidal Rule
#Using Created Functions

#True Integral Value: Calculated by Hand
trueValue = 4.4

#Trapezoidal Function with N=10
a = 0.0
b = 2.0
N = 10
k= 0.0
h = 0.0
s = 0.0

h = (b-a)/N

s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s+= f(a+k*h)

trapValue = h*s
trapError = abs(0.33333*(trueValue-trapValue))
    
print('\n')
print("The practical estimation of error using the trapezoidal rule ")
print("with N=10 on the function (x^4)-(2x)+1 yields")

print(trapError)


#Practical Estimation Errors: Simpson's Rule
#Using Created Functions

#Simpson's Rule with N=10
a = 0.0
b = 2.0
N = 10
k= 0.0
s = 0.0

x = a + h
for i in range(1, N/2 + 1):
    k += 4 * f(x)
    x += 2 * h

x = a + 2 * h

for i in range(1, N/2):
    k += 2 * f(x)
    x += 2 * h
    
simpsonValue = (h/3)*(f(a)+f(b)+k)
simpsonError = abs(0.06667*(trueValue-simpsonValue))
    
print('\n')
print("The practical estimation of error using Simpson's rule ")
print("with N=10 on the function (x^4)-(2x)+1 yields")

print(simpsonError)



