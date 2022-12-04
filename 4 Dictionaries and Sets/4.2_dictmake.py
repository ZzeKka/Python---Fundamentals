def dictmake(*args):
    if len(args)%2 != 0:
        return {}
    
    else:
        output = {}
        while args:
            output[args[0]] = args[1]
            args = args[2:] 
        return output
            


print(dictmake('a', 1, 'b', 2)) 