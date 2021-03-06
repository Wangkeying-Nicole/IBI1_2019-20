# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:55:06 2020

@author: 86158
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# define the basic variable
N=10000
rec=[0]
beta=0.3
gamma=0.05
#store the time for x 


for p in range (0,11):
 num_sus=int(N*(10-p)/10)
 sus=[num_sus]
 T=[0]
 t=0
 inf=[1]
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
 plt.plot(T,inf,label=str(p*10)+'%',color=cm.viridis(p*20))
 #show the legend
 plt.legend(loc='upper right')

#plot the picture
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.show()

#save the plot as image
plt.figure(figsize=(6,4),dpi =150)
plt.savefig('the SRI model', type='png')