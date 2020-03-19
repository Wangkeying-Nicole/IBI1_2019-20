# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:54:44 2020

@author: 86158
"""
#make a plt
import matplotlib.pylot as plt
import numpy as np

#Pie chart, where clices will be ordered and pollted countoe-clockwise
labels='A','C','T','G'
sizes=[6,4,5,6]
explode=(0,0,0,0)
#specifies the fraction of the radius with which to offset each wedge
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow=False,startangle=90 )
plt.axis('equal')
#equal aspect radio ensure that pie is drawn as a circle
plt.show()
