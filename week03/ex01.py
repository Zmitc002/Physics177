# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 3
# Problem 1


import numpy as np
from pylab import imshow,show


#PART A: ELECTRIC POTENTIAL

data = []
#Defining Potential Function
def potential(x,y):
    K = 111.266
    potentialNeg = (-1/(K*np.sqrt(((x+5)**2)+((y)**2))))
    potentialPos = (1/(K*np.sqrt(((x-5)**2)+((y)**2))))
    return potentialNeg + potentialPos

#Inputing Values into Potential for  1 X 1 Meter plane
for x in range (-50,50):
    for y in range (-50,50):
        float(x)
        float(y)
        
        data.append(potential(y,x))

#Potential Density Plot
print ("Density Plot for Potential: ")
data = np.reshape(data, (100, 100))    
imshow(data)
show()            
        
        
        
        
#PART B: ELECTRIC FIELD
        
data2 = []  
#Defining Electric Field Function
def electric(x,y):
    K = 111.266
    elecdx1=(2*(x+5))/(K*np.sqrt(((x+5)**2)+((y)**2))**3)
    elecdx2=(-2*(x-5))/(K*np.sqrt(((x-5)**2)+((y)**2))**3)
    elecdy1=(2*y)/(K*np.sqrt(((x+5)**2)+((y)**2))**3)
    elecdy2=(-2*y)/(K*np.sqrt(((x-5)**2)+((y)**2))**3)
    return elecdx1+elecdx2+elecdy1+elecdy2
    
#Inputing Values into Electric Field for 1 X 1 meter plane
for x in range (-50,50):
    for y in range (-50,50):
        float(x)
        float(y)
        data2.append(electric(y,x))
        
#Electric Field Density Plot
print ("Density Plot for Electric Field: ")
data2 = np.reshape(data2, (100, 100))    
imshow(data2)
show() 
