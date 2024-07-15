'''Write a program to prompt users to enter a year; then find 
whether it’s a leap year. A year is considered a leap year if it’s 
divisible by 4 and 100 and 400. If it’s divisible by 4 and 100 but 
not by 400, it’s not a leap year. Display a proper message.'''

LeapYear = int(input("Enter the year : "))
if LeapYear%4==0 and LeapYear%100!=0 :
    print(LeapYear,"is a leap year")
else :
    print(LeapYear,"not a leap year")
