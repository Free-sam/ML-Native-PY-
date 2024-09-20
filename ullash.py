# for having something that is very special #
j = [67,33,22,13,54,32,11]
#  attaching array in python #
print(type(j))
print(j)
# some operation #
print(max(j))
print(min(j))
print(len(j))
j.append(90)
print(j)
j.insert(3,80)
print(j)
j.pop(5)
print(j)
j.remove(22)
print(j)
u = (89,44,32,11,56,32)
o = list(u)
for h in u:
    print(h)

print(type(u))
print(type(o))
for h in range(0 ,6):
    print(o[h])
print("----::just traversing for only even numbers::---")
for y in range(0, 11):
    if(y%2==0):
        print(y)
print(("-----continue statement exists------"))
for y in range(0, 11):
    if(y==6):
        continue
    print(y)
print(("-----break statement exists------"))
for y in range(0, 11):
    if(y==6):
        break
    print(y)
# for looping statement #
print(id(u))
