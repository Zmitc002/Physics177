# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Final Project
# Diffusion Limited Aggregation on Square Center

import numpy as np
import matplotlib.pyplot as plt
from random import randrange

#Note that for presentation purposes 2D array was set to 401x401. Limits have been changed here, however,
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

#This is "trick" I made for plot iterations to be used in final animation. Not necessary for single plot.
#trick = "a"

#Completes cycle for each particle
for n in range(600):

    #Sets Spawning Location to random spot on perimeter
    randSide = randrange(1,5)
    if randSide == 1:
        a = randrange(1,99)
        b = 1
    if randSide == 2:
        a = randrange(1,99)
        b = 99
    if randSide == 3:
        a = 1
        b = randrange(1,99)
    if randSide == 4:
        a = 99
        b = randrange(1,99)

    image[a][b] = 1
    stuck = False

    for p in range(21):
        image[40][40+p] = 1
        image[40+p][40] = 1
        image[60][40+p] = 1
        image[40+p][60] = 1

    #Continues Cycle Until Stuck
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

            #This is the second component to the plot "trick" mentioned above. Not necessary for single plot.
            #if n % 500 == 0:

             #   trick = "a" + trick
             #   plt.imshow(image, cmap=plt.cm.bone,interpolation='nearest')
             #   plt.xlim(1,400)
             #   plt.ylim(1,400)
             #   plt.savefig(trick)

#Plots final state of simulation.
plt.imshow(image, cmap=plt.cm.bone,interpolation='nearest')
plt.xlim(1,100)
plt.ylim(1,100)
plt.savefig('DLA on Square Center')
