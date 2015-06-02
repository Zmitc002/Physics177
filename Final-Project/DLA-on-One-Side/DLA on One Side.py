# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Final Project
# Diffusion Limited Aggregation on One Side

import numpy as np
import matplotlib.pyplot as plt
from random import randrange

#Note that for presentation purposes 2D array was set to 401x401 and 801x801. Limits have been changed here, however,
#to 101x101. This allows for much faster processing with a less detailed simulation.

#Sets 2D Array to all zeros
image = []
for x in range(0,101):
    for y in range(0,101):
        image.append(0)

image = np.reshape(image,(101,101))

#Setting Boundaries to Off Limits. Note here that right vertical side is set to allow cell aggregation.
for i in range(0,101):
    image[0][i] = 2
    image[100][i] = 2
    image[i][0] = 2
    image[i][100] = 1

#Sets initial cell state to not stuck.
stuck = False

#This is "trick" I made for plot iterations to be used in final animation. Not necessary for single plot.
#trick = "a"

#For color variation
m = 0.1

#Main Sequence
#Completes cycle for each particle
for n in range(1200):

    #Spawning Location is random point along left vertical side.
    a = randrange(10,90)
    b = 3
    image[a][b] = 1

    #Resets state to not Stuck
    stuck = False

    #Continues Cycle Until Stuck
    while stuck == False:

        #Sets xmove, ymove to either -1, 0, or 1. Note that ymove cannot move backward here which speeds-up process.
        xmove =  randrange(1,4)
        ymove = randrange(1,3)

        if xmove == 2:
            xmove = -1
        if xmove == 3:
            xmove = 0
        if ymove == 2:
            ymove = 0

        #If cell moves to the upper or lower boundaries the trajectory is changed
        if image[a+xmove][b+ymove] == 2:

            #Repeats Loop until trajectory is not along upper or lower boundary.
            while image[a+xmove][b+ymove] == 2:

                #Sets xmove, ymove to either -1, 0, or 1. ymove cannot move backward here. Speeds-up process.
                xmove =  randrange(1,4)
                ymove = randrange(1,3)

                if xmove == 2:
                    xmove = -1
                if xmove == 3:
                    xmove = 0
                if ymove == 2:
                    ymove = 0

        #Keeps moving if there is no adjacent stuck particle
        image[a+xmove][b+ymove] = 1
        image[a][b] = 0
        a = a+xmove
        b = b+ymove

        #If there is an adjacent stuck particle this particle also becomes stuck
        if (image[a][b] != 2) and (image[a+1][b+1] != 0 or image[a+1][b-1] != 0  or image[a-1][b+1] != 0 \
                        or image[a-1][b-1] != 0 or image[a][b+1] != 0 or image[a][b-1] != 0 or image[a+1][b]!= 0 \
                            or image[a-1][b] != 0):
            p = n%101
            m += 1.*p
            image[a][b]= m
            stuck = True

            #This is the second component to the plot "trick" mentioned above. Not necessary for single plot.
            #if n % 2000 == 0:
            #    trick = "a" + trick
            #    plt.imshow(image, cmap=plt.cm.bone,interpolation='nearest')
            #    plt.xlim(1,100)
            #    plt.ylim(1,100)
            #    plt.savefig(trick)

#Plots final state of simulation.
plt.imshow(image, cmap=plt.cm.pink,interpolation='nearest')
plt.xlim(1,100)
plt.ylim(1,100)
plt.savefig('DLA-One Side')
