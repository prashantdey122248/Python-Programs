#Program to perform file handling using read(),write(),append().
'''fp1 = open("Program.txt","w")
fp1.write("These codes are for new file.")
fp1.close()

fp2 = open("Program.txt","r")
print(fp2.read())
fp2.close()

fp3 = open("Program.txt","a+")
fp3.write("You are using append mode.")
fp3.seek(0)
print(fp3.read())
fp3.close()'''

#Program to take user input a.file name,b.content
'''file = input("Enter your file name : ")
content = input("Enter your content for the file : ")

file_p1 = open(file,"w+")
file_p1.write(content)
file_p1.seek(0)
print(file_p1.read())
file_p1.close()

file_p2 = open(file,"r")
count = file_p2.read()
char = len(count)
print("Total character : ",char)
file_p2.close()'''


'''file_p2 = open(file,"r")
print(file_p2.read())
file_p2.close()'''


