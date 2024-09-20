#create a triangle#
g = int(input("enter the num:"))
for i in range(0, g):
    for j in range(0, i+1):
        print("*",end=" ")
    print(" ")
for i in range(0, g):
    for j in range(g, i, -1):
        print("*",end=" ")
    print(" ")