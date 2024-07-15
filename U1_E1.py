'''Program to take user input and create numeric list out of that list create two
different list,square and cube for odd and even values of list respectively'''
term = int(input("Enter value for terms : "))
list = []
square = []
cube = []
for a in range(term):
    num = int(input("Enter elements for the list :  "))
    list.append(num)

    if num%2==0:
        cube1 = num**3
        cube.append(cube1)
    else :
        square1 = num**2
        square.append(square1)
print(list)
print("Square is : ",square)
print("Cube is : ",cube)



        
