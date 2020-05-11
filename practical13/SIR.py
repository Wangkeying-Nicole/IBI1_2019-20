# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:52:15 2020

@author: 86158
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# define the basic variable
N=10000
sus=[9999]
inf=[1]
rec=[0]
beta=0.3
gamma=0.05
#store the time for x 
T=[0]

#random.choice function
#run the model for 1000 times
for t in range (0,1000):
    a=np.random.choice(range(2),sus[t],p=[1-beta*(inf[t]/N), beta*(inf[t]/N)])
    #count the number of people infected
    num_inf= np.sum(a == 1)
    b=np.random.choice(range(2),inf[t],p=[1-gamma,gamma])    
    #Count the number of people recovered
    num_rec= np.sum(b == 1)
    #record the output of each time step
    sus.append(sus[t]-num_inf)
    inf.append(inf[t]+num_inf-num_rec)
    rec.append(rec[t]+num_rec) 
    T.append(t)
    
    
#plot the picture
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.plot(T,sus,label='susceptible')
plt.plot(T,inf,label='infected')
plt.plot(T,rec,label='recovered')
#show the legend
plt.legend(loc='upper right')
plt.show()
#save the plot as image
plt.figure(figsize=(6,4),dpi =150)
plt.savefig('the SRI model', type='png')


