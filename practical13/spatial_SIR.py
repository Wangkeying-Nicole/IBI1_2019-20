# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:25:52 2020

@author: 86158
"""

  
# import necessary libraries 
import numpy as np 
import matplotlib . pyplot as plt
beta=0.3
gamma=0.05
# make array of all susceptible population 
population = np. zeros ( (100 , 100) )
outbreak = np.random. choice (range(100) ,2) 
population [ outbreak [0] , outbreak [ 1 ] ] = 1
plt.figure ( figsize =(6 ,4) , dpi=150) 
plt.imshow( population , cmap='viridis', interpolation='nearest')
for i in range (0,100):
    # point out all the infected ones
    infectedIndex = np.where(population==1)
    # run through all infected points, infect others around it
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours 
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! 
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    # refresh the infected data
    infectedIndex = np.where(population==1)
    #recovery of the infected ones
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        population[x,y]=np.random.choice(range(2),1,p=[1 - gamma,gamma])[0] + 1 
    #output for each loop
    plt.figure ( figsize =(6 ,4) , dpi=150) 
    plt.imshow( population , cmap='viridis', interpolation='nearest')