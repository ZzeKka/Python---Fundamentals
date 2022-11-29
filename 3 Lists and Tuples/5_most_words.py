#print the word with the most repeating words
from collections import Counter

def most_repeated_letter(word):
    return Counter(word).most_common(1)[0][1]
            
def word_with_most_repeated_letter(list):
    return max(list,key = lambda word: most_repeated_letter(word))
        
        
        
print(word_with_most_repeated_letter(['this', 'is', 'an', 'elementary', 'test', 'example']))
    