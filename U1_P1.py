#Program to take input from user and perform arithmetic operations.

Num1 = int(input("Enter first number : "))
Num2 = int(input("Enter second number : "))

choice=input("Enter the operation you want to perfrom +-*/% : ")
if choice=="+" :
    print("Addition of",Num1," and " ,Num2,"is",Num1 + Num2)
elif choice=="-" :
    print("Substraction of",Num1," and " ,Num2,"is",Num1 - Num2)
elif choice=="*" :
    print("Multiplication of",Num1," and " ,Num2,"is",Num1 * Num2)
elif choice=="/" :
    print("Division of",Num1," and " ,Num2,"is",Num1 / Num2)
elif choice=="%" :
    print("Modulus of",Num1,"and",Num2,"is",NUM1 % Num2)
else :
    print("Enter valid operation")

