# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Final Project
# Diffusion Limited Aggregation on Sides

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

#Setting Boundaries to Stuck
for i in range(0,101):
    image[0][i] = 1
    image[100][i] = 1
    image[i][0] = 1
    image[i][100] = 1

#Initializing Spawning Location
a = 100
b = 100
image[a][b] = 1

#Sets initial cell state to not stuck.
stuck = False

#Main Sequence
#Completes cycle for each particle
for n in range(1000):

    #Reset Center
    stuck = False
    a = 50
    b = 50

    #Continues Cycle Until Stuck.
    while stuck == False:

        #Sets xmove, ymove to either -1, 0, or 1.
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

        #Keeps moving if there is no adjacent stuck particle.
        if image[a+1][b+1] == 0 and image[a+1][b-1] == 0  and image[a-1][b+1] == 0 and image[a-1][b-1] == 0 and \
                        image[a][b+1]==0 and image[a][b-1]==0 and image[a+1][b]==0 and image[a-1][b]==0:

            image[a+xmove][b+ymove] = 1
            image[a][b] = 0
            a = a+xmove
            b = b+ymove

        #If there is an adjacent stuck particle this particle also becomes stuck.
        else:

            image[a][b]= 1
            stuck = True

plt.imshow(image, cmap=plt.cm.copper,interpolation='nearest')
plt.xlim(1,100)
plt.ylim(1,100)
plt.savefig("DLA-Sides")
