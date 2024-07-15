#Write python program to print following loops :
#a.1 2 3 4 5 6 ....10
'''num = int(input("Enter the end value of the loop : "))
for i in range(num):
    print(i,end=" ")'''

#b.2 4 6 8 10 ....20
'''num = int(input("Enter the end value of the loop : "))
for i in range(2,num,2):
    print(i,end=" ")'''

#c.1 3 5 7 ....19
'''num = int(input("Enter the end value of the loop : "))
for i in range(1,num,2):
    print(i,end=" ")'''

#d.100 99 98 ....90
'''num = int(input("Enter the end value of the loop : "))
for i in range(100,num,-1):
    print(i,end=" ")'''

#e.200 198 196 ....180
'''num = int(input("Enter the end value of the loop : "))
for i in range(200,num,-2):
    print(i,end=" ")'''

#f.0 1 1 2 3 5 8 ....n
ttl_terms = int(input("Enter the number of terms for fibonacci series : "))
a,b = 0,1
count = 0
if ttl_terms <= 0 :
    print("Please enter a positive interger.")
elif ttl_terms == 1 :
    print("Fibonacci series up to",ttl_terms,"terms : ",a)
else :
    print("Fibonacci series up to",ttl_terms,"terms : ")
    while count < ttl_terms :
            print(a,end=" ")
            lst_term = a + b
            a = b
            b = lst_term
            count += 1
    
    
