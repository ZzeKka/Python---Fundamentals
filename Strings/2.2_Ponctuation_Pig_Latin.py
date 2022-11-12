vowels = ['a','e','i','o','u']

def pig_latin_cap(str):
    if str[0].lower() in vowels:
        if(not str[-1].isalnum()):
            return f"{str[0:-1]}way{str[-1]}"
        else: 
            return f"{str}way"
    else:
        if(not str[-1].isalnum()):
            if(str[0].isupper()):
                return (f"{str[1]}{str[2:-1]}{str[0]}ay{str[-1]}".casefold()).capitalize()
            else:
                return f"{str[1:-1]}{str[0]}ay{str[-1]}".casefold()
        else:     
            if(str[0].isupper()):
                return (f"{str[1]}{str[2:]}{str[0]}ay".casefold()).capitalize()
            else:
                return f"{str[1:]}{str[0]}ay".casefold()
            
print(pig_latin_cap('ola!'))
print(pig_latin_cap('Boas.'))
print(pig_latin_cap('Culhos?'))  