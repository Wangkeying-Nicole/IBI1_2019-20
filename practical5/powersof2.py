# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:56:04 2020

@author: 86158
"""

#import number Y, variables x(changing), b(counting), a(marking down string)
temp=input('please input a number:')
Y=int(temp)
x=Y
b=0
a=""
#start a loop to count for the power of 2
#till x=0
while x!=0:
    b=b+1
#marking down when x%2==1
    if x%2==1:
        a="2**"+str(b-1)+"+"+a
        x=(x-1)/2
#move forward when x%2==0
    else:
        x=x/2
#output the result 
print(str(Y)+"is"+a[:-1])
    
