#becoming  a new driver#
a = input("enter the (married/unmarried)::")
b = input("enter the gender (M/F)::")
c = int(input("enter age::"))
if(a == "unmarried" and b =="M" ):
    print("not eligible")
elif(a == "unmarried" and b == "F"):
    print("eligible")
elif(a == "married" and b == "M" and c >= 35):
    print("eligible")
elif(a == "unmarried" and b  =="F" and c <= 35):
    print("eligible")
else:
    print("not eligible")