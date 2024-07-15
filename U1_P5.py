'''. Write a program to prompt users to enter their working hours 
and rate per hour to calculate gross pay. The program should 
give the employee 1.5 times the hours worked above 30 hours. If 
Enter Hours is 50 and Enter Rate is 10, then the calculated 
payment is Pay: 600.0 '''

Hour = int(input("Enter your working hours : "))
Rate = int(input("Enter rate per hour : "))
if Hour<=30 :
    print("Payment : ",Hour * Rate)
elif Hour>30 :
    print("Payment : ",30*Rate+(Hour-30)*1.5*Rate)
    
