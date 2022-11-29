vowels = ['a','e','i','o','u']

def pig_latin(str):
    if str[0].lower() in vowels:
        return f"{str}way"
    else:
        return f"{str[1:]}{str[0]}ay"

print(pig_latin('air'))
print(pig_latin('eat'))
print(pig_latin('python'))
print(pig_latin('computer'))