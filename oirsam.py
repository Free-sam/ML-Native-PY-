# lets do a prime function #
n = int(input("enter the number::"))
for i in range(1, n+1):
    if(i%2==0):
        print("even numbers are::",i)
j="odds are"
print(j.center(20,"0"))
for i in range(1, n + 1):
    if(i%2!=0):
        print("the odd numbers are::",i)

