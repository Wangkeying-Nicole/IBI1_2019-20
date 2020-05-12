# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:44:53 2020

@author: 86158
"""
#import a
a=151
b=151151
b%7
#calculate c, d, e
c=b/7
d=c/11
e=d/13
print("e="+str(e))
#compare with a
if e>a:
    print('e>a')
elif e==a:
    print('e=a')
else:
    print('e<a')

#import X, Y, Z ,W as booleans
#the value of X and Y can be changed
X=False
Y=True
#calculate the value of Z
Z=(X and not Y)or(Y and not X)#when X or Y is True(not both), Z is true
print("Z="+str(Z))
#calculate the value of W
W=(X!=Y)
print("W="+str(W))
#comparison between W and Z
if W==Z:
    print('W and Z are the same')
if W!=Z:
    print('W and Z are different')