#Python program to handle simple runtime error
"""
a = 10
b = 0

try :
    print(a/b)
except Exception as e :
    print(e)
print("You have envoked arithmetic exception.")
"""

#write a program to generate arithmetic exception and log the exception in system.
import logging

a = 10
b = 0

try :
    print(a/b)
except Exception as Argument :

    f = open("demo.txt","w")
    f.write(str(Argument))
    f.write(str("  Arithmetic exception logged"))

    f.close()
    
