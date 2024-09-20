f = ["56","45","89","100"]
z = ["67","78","32","90"]
print(type(f))
#that is how it will insert#
a = f.append("234")
print(f)
b = f.insert(2,"46")
print(f)
#that is how it will remove#
c = f.remove("89")
print(f)
d = f.pop(4)
print(f)
#if we extened the list then it will act like this way#
f.extend(z)
print(f)
#if we added some item in tuple then we have to write on thsi way#
j = ("67","89","12","89")
print(j)
print(type(j))
#for it traverse#
for k in j:
    print(k)


