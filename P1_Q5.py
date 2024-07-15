#Write a program to prepare marksheet with total,percentage,result and class.
num1 = int(input("Enter Marks of Maths : "))
num2 = int(input("Enter Marks of Physics : "))
num3 = int(input("Enter Marks of Chemistry : "))

total = num1 + num2 + num3
per = total/300*100

if per>=80:
    print("First Class with",per,"percentage")
elif per>=60 and per<80:
    print("Second Class with",per,"percentage")
elif per>=40 and per<60:
    print("Pass with",per,"percentage")
else :
    print("You are failed")

