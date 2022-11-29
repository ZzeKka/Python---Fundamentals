from collections import Counter
#checks the word with most repeated vowels
def most_vowels(word):
    c = Counter(word)
    max = 0
    for key in c:
        if key in 'aeiou' and c[key] > max:
            max = c[key]
    return max

def most_repeated_vowel_word(list):
    return max(list, key = most_vowels)

print(most_repeated_vowel_word(['thisisthis', 'is', 'an',
'elementary', 'test', 'example']))
