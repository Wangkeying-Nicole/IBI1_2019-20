# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:44:48 2020

@author: 86158
"""

#number input
number = input("Please input numbers to compute 24: (use ',' to divide them)")
num = []
flag=True
for items in number.split(","):
   num.append(float(items))
for items in num:
   if ((items > 23) or (items < 1)):
       flag=False
       print(str(items)+" is not between integers 1 to 23."+'The input number must be integers from 1 to 23 ')
       break
   
# ser up function to list all the possible situations of the arrangement and the selection
def select_calc(l: int):
   return_list = []
   for i in list(range(l-1)):
      for j in list(range(i+1,l)):
          for k in range(6):
             return_list.append([i, j, k])
   return (return_list)
#store the possible arrangement in a list 
sc = [[], []]
for i in range(2, len(num) + 1):
   sc.append(select_calc(i))
sci = []
for i in range(len(num)):
   sci.append(sc[len(num) - i])
   
# set up function to select one operation [] from one stage.
all_sit = []
def select_copy(l: list):
   l_copy = l.copy()
   if len(l_copy) == len(sci) - 1:
      all_sit.append(l_copy)
   for item in sci[len(l)]:
      l.append(item)
      select_copy(l)
      l.pop()
   
select_copy([])
 
# set up function to run the calculation
def select_apply(i:int, j:int, k:int, l:list):# k indicates the 6 operations 
    out=0 
    if (k == 0):
        out = l[i] + l[j]
    elif (k == 1):
        out = l[i] - l[j]
    elif (k == 2):
        out = l[j] - l[i]
    elif (k == 3):
        out = l[i] * l[j]
    elif (l[j] != 0) and (l[i] != 0) :
        if (k == 4):
            out = l[i] / l[j]
        else:
            out = l[j] / l[i]
    if (out == 24):
        return (0)#finish
    else:
        l[i] = out
        l.pop(j)
        return (1)#continue to find
a=0 #mark if 24 has got  
n = 1
if flag==True:
 for item in all_sit:
   num_copy=num.copy()
   for jtem in item:
       if (select_apply(jtem[0], jtem[1], jtem[2], num_copy) ==0 ) and a == 0:
          print("Yes")
          print("recursion times: " + str(n))
          a=1
       else:
          n = n + 1
 if a == 0:
    print("No")