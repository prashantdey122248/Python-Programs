"""Write a program to create a list of names; then define a function 
to display all the elements in the received list. Call the function to 
execute its statements and display all names in the list."""
lst = []
term = int(input("Enter how many terms you want : "))
for i in range(term):
    name = input("Enter names for your list : ")
    lst.append(name)
print(lst)
