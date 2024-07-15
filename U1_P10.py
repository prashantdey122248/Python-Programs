'''Write a program to prompt users to enter a Fibonacci 
sequence.'''

num1 = 0
num2 = 1
terms = int(input("Enter number of terms you want : "))
print(num1,num2,end=" ")
for i in range(terms):
    num3 = num1 + num2
    print(num3,end=" ")
    num1 = num2
    num2 = num3
