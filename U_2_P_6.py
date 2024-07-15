'''Python program to read numbers from  a file and then calculate the maximum and
minimum out of it.'''

numbers = []
with open(r'F:\122248MCA2B\Python\Question6.txt','r') as file:
    for line in file:
        try:
            number = float(line.strip())
            numbers.append(number)
        except ValueError:
            print("Skipping non_numeric value : ",line.strip())
    

if numbers:
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print("Total : ",total)
    print("Maximum : ",maximum)
    print("Minimum : ",minimum)
else :
    print("No numbers found in the file.")




    
