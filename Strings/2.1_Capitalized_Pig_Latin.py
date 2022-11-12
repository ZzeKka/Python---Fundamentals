vowels = ['a','e','i','o','u']

def pig_latin_cap(str):
    if str[0].lower() in vowels:
        return f"{str}way"
    else:
        if(str[0].isupper()):
            str = f"{str[1]}{str[2:]}{str[0]}ay".casefold()
            return str.capitalize()
        else:
            return f"{str[1:]}{str[0]}ay".casefold()

print(pig_latin_cap('ola'))
print(pig_latin_cap('Boas'))
print(pig_latin_cap('Culhos'))  
        