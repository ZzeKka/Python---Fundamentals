#returns the first and last element mantaining input format
def first_last(input):
    return input[:1] + input[-1:] 

print(first_last('abcd'))
print(first_last([1,2,3,4]))
print(first_last((1,2,3)))