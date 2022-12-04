d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}

all_keys = d3.keys() | d4.keys()
print(type(d3.keys()))
print(all_keys)
print(type(all_keys))