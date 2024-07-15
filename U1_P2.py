'''Write a Python script to prompt users to enter the first and last 
values and generate some random values between the two 
entered values.'''

import random

Num = int(input("Enter total number of random numbers you want : "))
Llimit = int(input("Enter lower limit : "))
Ulimit = int(input("Enter upper limit : "))
for i in range(Num):
    num = random.randint(Llimit,Ulimit)
    print(num)
             
