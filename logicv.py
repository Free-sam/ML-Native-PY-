sam = open("happy.txt","w")
l = ["happy now \n","u are awesome\n","u are the best"]
sam.writelines(l)
sam.close()

#let's make a program that to delete the vowels from a specific string name#
kola = "it is a kola"
##here the program to remove the vowels from string##
def remove_vowels(string):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    result=" "
    for chars in string:
        if chars not in vowels:
            result+=chars
    return result
string = "hello mogambo"
modified_string = remove_vowels(string)
print((modified_string))

