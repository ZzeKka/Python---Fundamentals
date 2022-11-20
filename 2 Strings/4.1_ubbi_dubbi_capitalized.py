def hubbi_dubbi_capitalized(word):
    output = []
      
    for letter in word:

        if(letter.casefold() in 'aeiou' ):
            output.append(f'ub{letter}')
        else:
            output.append(f'{letter}')
            
    if word[0].isupper():
        output[0] = output[0].capitalize()
    return ''.join(output)

print(hubbi_dubbi_capitalized('Octupus'))