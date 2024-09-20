import random
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
print(ul)