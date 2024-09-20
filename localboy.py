salary=int(input("enter the value of salary::"))
df= int(input("enter the input of df::"))
hra=int(input("enter the input of hra::"))
if(df>=50 and hra>=30):
    df1 = (salary * df) / 100
    hra1 = (salary * hra) / 100
    total1 = df1 + hra1 + salary
else:
    df2 = 500
    hra2 = (salary * hra) / 100
    total2 = df2 + hra2 + salary
if(salary>=1500):
    print("the total ammount:",total1)
elif(salary<1500):
    print("the total value will be:",total2)