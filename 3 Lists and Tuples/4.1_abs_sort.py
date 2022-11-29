#order a list of numbers by absolute value

def abs_sort(list):
    return sorted(list,key = abs)

print(abs_sort([10,-20,1,-2,5]))    