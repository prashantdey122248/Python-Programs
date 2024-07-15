#Program to find simple interest and compound interest using user input.
p = int(input("Enter principle amount : "))
r = float(input("Enter rate of interest : "))
t = int(input("Enter time in years : "))
n = int(input("Enter number of times compounded per time : "))
SI = p*r*t/100
CI = round(p*(1+r/100)**n-p)
print(SI)
print(CI)
