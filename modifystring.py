#let's read a quick recap of datatypes of python#
#slicing#
a="hello u are good"
print(a[0:9])
####string modification####
#upppercase#
a="katacomb"
print(a.upper())  #we can write another syntaxial behavior using another var#
b="HDIDIID"
print(b.lower())
j=" hello world sheknoy "
print(j.strip())
#for replacing##
k="holoram"
print(k.replace("l","i"))
#string concatination#
a="hyh"
b="kola"
print(a + " " + b)
#formating string##
age =45
color = "yellow"
food = "momo"
sam="i am sam and my age limit is == {0} my fav food is == {1} and fav color is == {2}"
print(sam.format(age,food,color))
#escape character#
txt="that is very good to \'me\' cause it have a pursuital behavior"
print(txt)
print("that u are so beautiful \"that's\" why u are a good in behavior")
print("that u are so beautiful \athat's\a why u are a good in behavior")
print("that u are so beautiful \fthat's\f why u are a good in behavior")

a="hapPynow that is very good to"
print(a.capitalize())
print(a.upper())
print(a.casefold())
print(a.center(40,"-"))
print(a.count("that",0,20))
print(a.encode())
print(a.endswith("to",7,29))
print(a.isascii())
print(a.isprintable())
l="copl"
print(l.isalpha())
print(l.index("p"))
ko="50"
print(ko.zfill(10))
print(l.zfill(10))
p = ["yhh","78","jjdj"]
j = "hdhh"
print(type(p))
o = j.join(p)
print(o)