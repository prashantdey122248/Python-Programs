#wap of result

def student(m1,m2,m3,m4,m5):
    total=m1+m2+m3+m4+m5
    print('total is:',total)

    per=total/5
    print('percentage is:',per)

    if per>=70 and per<=40:
        print("pass")
    elif per>=70:
        print("result is pass")
    else:
        print("fail")
    
m1=int(input("enter the marks:"))
m2=int(input("enter the marks:"))
m3=int(input("enter the marks:"))
m4=int(input("enter the marks:"))
m5=int(input("enter the marks:"))

student(m1,m2,m3,m4,m5)

