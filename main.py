##for series prime##
u = int(input("enter the upper limit value::"))
for i in range(1, u+1):
    flag=0
    for j in range(2, (i//2)+1):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print(i,end=" 10")