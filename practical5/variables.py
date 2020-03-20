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
print(e)
#compare with a
if e>a:
    print('e>a')
elif e==a:
    print('e=a')
else:
    print('e<a')

#import X, Y, Z ,W as booleans
X=False
Y=True
Z=(X and not Y)or(Y and not X)
print(Z)
W=(X!=Y)
print(W)