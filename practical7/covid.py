# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:10:52 2020

@author: 86158
"""
#import necessary libraries
import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

#importing the .csv file
os.chdir(r"D:\learning material\IBI1 8011\Pratical\IBI1_2019-20\practical7")
covid_data=pd.read_csv("full_data.csv")
#showing all column, and every third rows between (and including) 0 and 15
print(covid_data.iloc[0:16:3,:])
#used a Boolean to show “total_cases” for all rows corresponding to Afghanistan
columns_1 = [False, True, False, False, True,False] 
b= covid_data.iloc[:,columns_1]
a=b.values
for i in range(len(b)):
    if a[i,0] == 'Afghanistan':
        print(a[i,:])
    else:
        continue

#read the data needed for calculating the mean and median, and the plot
columns_2 = [True, True, True, True, False,False] 
c= covid_data.iloc[:,columns_2]
d=c.values
list_1=[]
list_2=[]
list_3=[]
for i in range(len(b)):
    if d[i,1] == 'World':
        list_1.append(d[i,2])#new case
        list_2.append(d[i,0])#date
        list_3.append(d[i,3])#new death

wnc=np.array(list_1) #wnc=world new cases
wd=np.array(list_2)  #wd=world date
wnd=np.array(list_3)  #wnd=world new deaths
#computed the mean and median of new cases for the entire world 
c=np.mean(wnc)
d=np.median(wnc)
print('the mean is '+ str(c))
print('the median is '+ str(d))

#created a boxplot of new cases worldwide   
score=wnc
plt.boxplot(score,vert=True,whis=1.5,patch_artist=True,meanline=False)
plt.title("a boxplot of new cases worldwide")
plt.ylabel("new cases")
plt.show()

#plotted both new cases and new deaths worldwide
plt.figure(figsize=(8,3),dpi=80)
plt.plot(wd,wnc,label='world new cases',color='blue',linestyle='-',linewidth=3)
plt.plot(wd,wnd,label='world new deaths',color='red',linestyle='--',linewidth=3)
plt.legend(loc='upper left')
plt.xticks(list_2[0:len(list_2):4],rotation=-90)
plt.xlabel("date")
plt.ylabel("numbers")
plt.title("new cases and new deaths worldwide")
plt.show()

#There is the code to answer the question in txt: 
#How have new cases and total cases developed over time in Spain? 
#read necessary data
columns_3 = [True, True, True, False, True, False] 
c= covid_data.iloc[:,columns_3]
d=c.values
list_4=[]
list_5=[]
list_6=[]
for i in range(len(b)):
    if d[i,1] == 'Spain':
        list_4.append(d[i,2])#new case
        list_5.append(d[i,0])#date
        list_6.append(d[i,3])#total case
nc=np.array(list_4)
d=np.array(list_5)
tc=np.array(list_6)
#plot the figure of total cases and the new cases
plt.figure(figsize=(8,3),dpi=80)
plt.plot(d,nc,label='new cases',color='orange',linestyle='-',linewidth=3)
plt.plot(d,tc,label='total cases',color='red',linestyle='--',linewidth=3)
plt.legend(loc='upper left')
plt.xticks(list_2[0:len(list_2):4],rotation=-90)
plt.xlabel("date")
plt.ylabel("numbers")
plt.title("new cases and total case in Spain")
plt.show()
#plot the figure of new case alone to have a better view of the tendency.
plt.figure(figsize=(8,3),dpi=80)
plt.plot(d,nc,label='new cases',color='orange',linestyle='-',linewidth=3)
plt.legend(loc='upper left')
plt.xticks(list_2[0:len(list_2):3],rotation=-90)
plt.xlabel("date")
plt.ylabel("numbers")
plt.title("new cases and total case in Spain")
plt.show()
max_newcases=max(list_4)
print("The max daily new cases is "+str(max_newcases))


