def ubbi_dubbi(word):
    output = f""
    for letter in word:
        if letter in 'aeiou':
            output += f"ub{letter}"
        else:
            output += f"{letter}"
    return output

print(ubbi_dubbi("octopus"))