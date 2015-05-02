# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 5
# Problem 1

from pylab import plot,xlim,show,ylim,savefig
from numpy import linspace


#PART A: Plotting Polynomial, Saving as .PNG File, Finding Roots by
#Visual Inspection
 
print('\n')
print("PART A: Polynomial Plot ")

x = linspace(0,1)
y = 924*x**6-227*x**5+3150*x**4-1680*x**3+420*x**2-42*x+1
plot (x,y)


xlim(.02,.16)
ylim(-0.5,0.5)
savefig('Polynomial_Plot.png')
show()


print('\n')
print("The roots of the polynomial appear to be: ")
print("x = 0.034 and x = 0.145")


#PART B: Newton's Method

print('\n')
print("--------------------------------------------------")
print("PART B: Finding Roots Using Newton's Method ")
print('\n')
print("Using Newton's Method the Polynomial's Roots Are: ")

accuracy = 1e-10

def f(x):
    return 924*x**6-227*x**5+3150*x**4-1680*x**3+420*x**2-42*x+1
    
def dy(x):
    return 22080*x**5-1135*x**4+12600*x**3-5040*x**2+840*x-42
    
def newton(x):
    
    a = x
    delta = 1.0
    roots = []
    
    while abs(delta) > accuracy:
        delta = f(x)/dy(x)
        x -= delta
        
    roots.append(x)
    x = a + 1.0
    delta = 1.0
    
    while abs(delta) > accuracy:
        delta = f(x)/dy(x)
        x -= delta
        
    roots.append(x)
    return roots
    
print(newton(0.0))






