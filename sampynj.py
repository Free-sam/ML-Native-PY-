import math
import random
print(math.factorial(5))
x=4
p = math.sqrt(x)
print(p)                #for sqrt purpouse#
z = math.degrees(2*(math.pi))
print(z)
print(math.fabs(x))     #absolute factorial#
print(math.log(x))      #log basis#
print(math.log10(x))    #log10 basis#
print("the exp of ",x," will be::",math.exp(x))
print(math.trunc(x))        #same all down faces are#
print(math.floor(x))        ###                     ###
print(math.ceil(x))         ###                     ###

m = 90
n = 78
k = "hello"
print(id(m))
print(id(n))
print(isinstance(m,int),isinstance(n,float))
print(m+n,k)
print(k.isalpha())
print(k.replace("e","m"))
print(k.isprintable())
print(k.center(30,"-"))
print(k.endswith("0",0,4))
print(k.index("e",0,4))
print(k.count("l",0,4))