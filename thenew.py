def remove_vowels(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    result=" "
    for char in string:
        if char not in vowels:
            result = result + char
    return result
string = "hello sam"
mstring = remove_vowels(string)
print(mstring)