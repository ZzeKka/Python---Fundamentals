def bigger_sum(limit,*args):
    if not limit:
        return limit
    output = False
    for a in args:
        if(output == False and a > limit):
            output = a
        elif a > limit:
            output += a
    return output

print(bigger_sum(10, 5, 20, 30, 6))
print(bigger_sum('c','dazdfbg','a','zz'))