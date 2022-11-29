#adds and subtracts numbers from a list
def plus_minus(input):
    sum = input[0]
    count = 1
    for n in input[1:]:
        if count%2 != 0:
            sum += n
        else:
            sum -= n
        count += 1
    return sum

print(plus_minus((10,20,30,40,50,60)))