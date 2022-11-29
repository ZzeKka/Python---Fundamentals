#sum al elemtents that are or can be turned into ints
def numeric_sum(*args):
    sum = 0
    for a in args:
        try:
            sum += int(a)
        except ValueError:
            continue    
    return sum





print(numeric_sum(10, 20, 'a', '30',
'bcd'))  
