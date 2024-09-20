import random
h = random.randint(90,100)
print(h)

# let add numbers that have highest limit #
s=0
for i in range(0, 11):
    s=s+i
print(s)
# pattern numbers #
n = int(input("enter the value of n::"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
for i in range(1, n + 1):
    for k in range((n+1)-1,i,-1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print("\n")

