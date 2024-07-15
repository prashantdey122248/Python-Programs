#WAP to create list and display 12 functions and methods for list.
lst = []
term = int(input("Enter number of terms : "))
for i in range(term):
        num = int(input("Enter your list elements : "))
        lst.append(num)
print(lst)
choice = int(input("Enter your choice : ","1.Access any index ,\n2.Update list,\n3.Delete element,\n4."))
