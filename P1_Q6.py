#Write a python program to enter two numbers and find maximum out of it.
'''num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if num1>num2:
   print(num1,"is greater than",num2)
else :
    print(num2,"is greater than",num1)'''

#Write a python program to enter three numbers and find maximum out of it.
'''num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if num1>num2 and num1>num3:
    print(num1,"is greater than",num2,"and",num3)
elif num2>num1 and num2>num3 :
    print(num2,"is greater than",num1,"and",num3)
else :
    print(num3,"is greater than",num1,"and",num2)'''

#Write a python program to enter 10 numbers and find sum and average of it.
'''total = 0
avg = 0
for i in range(1,11):
    num = int(input("Enter your prefered numbers : "))
    total = total + num
    avg = total / 10
print("Sum of number is : ",total,"Average of numbers is : ",avg)'''

#Write a python program to enter 10 numbers and find maximum out of it without using array.
max_num = 0
for i in range(1,11):
    num = int(input("Enter your prefered numbers : "))
    if num > max_num:
        max_num = num
print("Maximum is : ",max_num)

    
