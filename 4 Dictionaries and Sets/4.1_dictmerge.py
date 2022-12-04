def dictmerge(*dicts):
    output = {}
    
    for dict in dicts:
        output.update(dict)    
    return output 

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
d5 = {'a':1, 'b':2, 'd':4}

#output should be {'a':1, 'b':2,'c':4 ,'d':4}

print(dictmerge(d1,d2,d3,d4,d5))