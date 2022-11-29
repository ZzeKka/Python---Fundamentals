#returns a list of sum o even index numbers and odd index numbers
def even_odd(input):
    even_sum = 0
    for n in input[0::2]:
        even_sum += n
    odd_sum = 0
    for n in input[1::2]:
        odd_sum += n
    return [even_sum,odd_sum]
            
print(even_odd([1,2,3,4,5]))