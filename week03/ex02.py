# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 3
# Problem 2

from numpy import array, empty
from numpy.linalg import solve

#PART A: Equations for junctions with unknown voltages
A = array([[ 4, -1, -1, -1],
           [ -1, 3,  0, -1], 
           [ -1, 0,  3, -1],
           [ -1, -1, -1, 4]], float)
           
v = array([5, 0, 5, 0])
N = len(v)

print ('\n')
print ("PART A. Equations for junctions with unknown voltages in ")
print ("matrix form is: ")
print ('\n')
print A

#PART B: Solution for 4 Voltages using Gaussian Elimination
for m in range(N):
    
    #Divide by the diagonal element
    div = A[m,m]
    A[m,:] /=div
    v[m] /= div

    #Now subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

#Backsubstitution
x = empty(N, float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

print ('\n')
print ("PART B. Using Gaussian elimination the four voltages are: ")
print(x)            

#PART C: Solution for 4 Voltages using LU method and employing the 
        #function solve from numpy.linalg

print ('\n')
print ("PART C. Using LU decomposition the four voltages are: ")
x = solve(A,v)
print(x)
