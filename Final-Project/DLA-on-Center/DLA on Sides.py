# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Final Project
# Diffusion Limited Aggregation on Center

import numpy as np
import matplotlib.pyplot as plt
from random import randrange

#Note that for presentation purposes 2D array was set to 401x401 and 801x801. Limits have been changed here, however,
#to 101x101. This allows for much faster processing with a less detailed simulation.

#Sets 2D Image Array to all zeros
image = []
for x in range(0,101):
    for y in range(0,101):
        image.append(0)

image = np.reshape(image,(101,101))

#Setting Boundaries to Off Limits
for i in range(0,101):
    image[0][i] = 2
    image[100][i] = 2
    image[i][0] = 2
    image[i][100] = 2

#Sets initial cell state to not stuck
stuck = False

# This is the first component of a "trick" I made for plot iterations to be used in final animation.
# Not necessary for single plot.
#trick = "a"

#Completes cycle for each particle
for n in range(800):

    #Sets Spawning Location to random spot on perimeter
    randSide = randrange(1,5)
    if randSide == 1:
        a = randrange(1,100)
        b = 1
    if randSide == 2:
        a = randrange(1,100)
        b = 99
    if randSide == 3:
        a = 1
        b = randrange(1,100)
    if randSide == 4:
        a = 99
        b = randrange(1,100)

    image[a][b] = 1

    #Sets Cell State to not stuck
    stuck = False

    #Center Seed
    image[50][50]= 1

    #Continues cycle until stuck
    while stuck == False:

        #Sets xmove, ymove to either -1, 0, or 1
        xmove =  randrange(1,4)
        ymove = randrange(1,4)

        if xmove == 2:
            xmove = -1
        if ymove == 2:
            ymove = -1
        if xmove == 3:
            xmove = 0
        if ymove == 3:
            ymove = 0

        #If cell moves to the perimeter trajectory is changed
        if image[a+xmove][b+ymove] == 2:

            while image[a+xmove][b+ymove] == 2:

                #Sets xmove, ymove to either -1, 0, or 1
                xmove =  randrange(1,4)
                ymove = randrange(1,4)
                if xmove == 2:
                    xmove = -1
                if ymove == 2:
                    ymove = -1
                if xmove == 3:
                    xmove = 0
                if ymove == 3:
                    ymove = 0

        #Keeps moving if there is no adjacent stuck particle
        image[a+xmove][b+ymove] = 1
        image[a][b] = 0
        a = a+xmove
        b = b+ymove

        #If there is an adjacent stuck particle this particle also becomes stuck
        if image[a][b] != 2 and (image[a+1][b+1] == 1 or image[a+1][b-1] == 1  or image[a-1][b+1] == 1 \
                        or image[a-1][b-1] == 1 or image[a][b+1]== 1 or image[a][b-1]== 1 or image[a+1][b]== 1 \
                            or image[a-1][b]== 1):

            image[a][b]= 1
            stuck = True

            #This is the second component to the plot trick mentioned above. Not necessary for single plot.
            #trick = "a" + trick
            #plt.imshow(image, cmap=plt.cm.copper,interpolation='nearest')
            #plt.xlim(.5,19.5)
            #plt.ylim(.5,19.5)
            #plt.savefig(trick)

#Plots final state of simulation
plt.imshow(image, cmap=plt.cm.copper,interpolation='nearest')
plt.xlim(.5, 99.5)
plt.ylim(.5, 99.5)
plt.savefig('DLA-Center')
