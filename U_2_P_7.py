'''WAP to copy a text file using file handling mechanism.'''

with open(r'F:\122248MCA2B\Python\MyFile.txt','r') as file:
    with open('out.txt','w') as file1:
        for line in file:
            file1.write(line)
