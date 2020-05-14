# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:43:47 2020

@author: 86158
"""

#method for counting#1 import sequence d
DNA='ATGCTTCAGAAAGGTCTTACG'
d={}
for b in DNA:
    d[b]=(d[b]+1) if (b in d) else(1)#'A''C''T''G'store separately
print (d)#output the amount of the 

#method for counting#2 import sequence d
str='ATGCTTCAGAAAGGTCTTACG'
str=','.join(str)
d={}
list=str.split(',')#turn into a list——>count
for i in list:
    d[i]=list.count(i)#'A''C''T''G'store separately
print(d)

import matplotlib.pyplot as plt
#Pie chart, where clices will be ordered and pollted countoe-clockwise
labels=['A','C','T','G']
sizes=[d["A"],d["C"],d["T"],d["G"]]
explode=(0,0,0,0)
#specifies the fraction of the radius with which to offset each wedge
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow=False,startangle=90 )
plt.axis('equal')
#equal aspect radio ensure that pie is drawn as a circle
plt.show()
