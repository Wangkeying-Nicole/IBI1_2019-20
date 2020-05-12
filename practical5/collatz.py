# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:31:08 2020

@author: 86158
"""
#import n, start the loop
temp=input('please input a positive integer:')
n = int(temp)
print(n,"-")
while n>1 :
#judge n even or odd, give different operations
   #if the number is even
   if n%2==0:
      n=n/2
      print(n,"-")
   #if the number is odd
   else:
      n=n*3+1
      print(n,"-")

      