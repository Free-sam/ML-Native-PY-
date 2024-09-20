import random
import math
l = [12,44,56,32,45,78,99,21,11,90]    #list#
even=0
odd=0
print(random.random())
print("the list elements are::")
for i in l:
    print(i,end=" ")
for i in l:
    if i%2 == 0:
        even+=1
    elif i%2 != 0:
        odd+=1
print("\nthe odd numbers are",odd)
print("the even numbers are",even)


#alternative programme#
print(" let's build a  programmme on set:: ")
sam =[67,21]
for i in range(len(sam)):
    print(i)  #for printing index#
print(" elements prints :- : ")
for j in sam:
    print(j,end=" ")  #for printing elements in particular indexing#
das = {12,34,33,12,67,80}    #set#
print("\n")
for h in range(len(das)):
    print(h)
print(type(das))
print(das)
das.add(24)
das.add(90)
das.remove(12)
print(das)
das.pop()
print(das)
das.clear()
print(das)
ul = {12,'happy',90,11,34} #it can handle multiple elements#
print(ul,end=" ")
print("\n")
for k in ul:             #it can iterable also#
    print(k,end=" ")
#frozenset creativity#
print("\n")
s = frozenset({78,32,11,34})     #it is immutable so no chanehe is possible in this set#
print(type(s))
print(s)
list1=[67,21,33,222,13,89]
print(list1)
print(type(list1))
set2=set(list1)
print(type(set2))
print(set2)    #it is unordered collection , mutable , iterable/chnagable #
for i in range(len(set2)):
    print()
skanda=frozenset({34,78,54,54,32,44,67})
print(type(skanda))
print(skanda)
fro3=frozenset(set2)
print(type(fro3))
print(fro3)

print(fro3.issubset(skanda))
print(fro3.issuperset(skanda))
print(fro3.isdisjoint(skanda))


print(max(set2))
print(min(set2))
print(sorted(set2))
print(len(set2))
print(sum(set2))
print(all(set2))
print(any(set2))

x=pow(2,4)
u = divmod(5,9)
print(x)
print(u)
p = abs(23.54332)
print(p)
o = 90
print(math.sqrt(o))
print(math.modf(o))
print(math.log(4)) #floor,ceiling,truncate etc#
print()