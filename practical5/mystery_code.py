# What does this piece of code do?
# Answer: find a random number n that is prime. The the range of possible random prime is from 1 to 100.

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    #supposed the number is prime
    p=True
    #get a random number 1<=n<100 
    n = randint(1,100)
    #u=higher intenger of n square root
    u = ceil(n**(0.5))
    #judege if n can be devided evenly by the integer larger than 2, and smaller than u
    for i in range(2,u+1):
        if n%i == 0:
            p=False


     
print(n)
