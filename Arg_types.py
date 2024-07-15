#Creating function for required and keyword arguments.
def exam(year,sem,course,regular):
    print("Year : ",year,"Sem : ",sem,"Course : ",course,"Regular : ",regular)

#Regular arguments : 
exam("2022-23",1,"MCA1","True") 
exam("2023-24",2,"MCA2","False")
exam("2024-25",3,"MCA3","True")

print("\n")

#Keyword arguments :
exam(year="2022-23",sem=1,course="MCA1",regular="True")
exam(sem=2,year="2023-24",course="MCA2",regular="False")
exam(course="MCA3",year="2024-25",sem=3,regular="True")

#Creating function for default argument.
#With all default values
def product(p_id="00",p_name="SmartPhone",p_price="20000",p_company="Phone"):
    print("P_id : ",p_id,"P_name : ",p_name,"P_price : ",p_price,"P_company : ",p_company)

product()

#with 1 default value
def product(p_id,p_name,p_price,p_company="Phone"):
    print("P_id : ",p_id,"P_name : ",p_name,"P_price : ",p_price,"P_company : ",p_company)

product("01","J2","10000")

#with 2 default values
def product(p_id,p_name,p_price="15000",p_company="Phone"):
    print("P_id : ",p_id,"P_name : ",p_name,"P_price : ",p_price,"P_company : ",p_company)

product("02","J7")

#with 3 default values
def product(p_id,p_name="SmartPhone",p_price="10000",p_company="Phone"):
    print("P_id : ",p_id,"P_name : ",p_name,"P_price : ",p_price,"P_company : ",p_company)

product("03")

print("\n")

#Creating function for variable length argument:'*'(It will print in tupel form)
def StudentData(name,*details):
    print("Name : ",name,"Details : ",*details)

StudentData("Rohit",20,"Sem-2","BCA","Rajkot")

#Variable length argument with keyword argument:'**'(It will print in dictionary format)
def StudentData(**details):
    print("Details : ",details)

StudentData(Name="Mohit",Age=21,City="Bhopal",Course="MCA2")






