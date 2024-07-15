#Program to check whether the user is child,teenager,adult or a senior by their age.
age = int(input("Enter your age : "))
if age>=1 and age<=12 :
    print("User is a child who is",age,"year old")
elif age>12 and age<20 :
    print("User is a teenager who is",age,"year old")
elif age>19 and age<60 :
    print("User is an adult who is",age,"year old")
else :
    print("User is a senior citizen who is",age,"year old")
