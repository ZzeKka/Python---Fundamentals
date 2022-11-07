hexa = input("choose hexadecimal number: ")
decimal = 0
for exponent,algorism in enumerate(reversed(hexa)):
    decimal += ((16 ** exponent) * int(algorism))
print(decimal)