#checks the last word alphabethicly in a file
def last_word_alpha(filename):
    words = []
    for line in open(filename):
        str = line.split()
        for word in str:
            words.append(word)
    words = sorted(words)
    return words[-1]
    
print(last_word_alpha("boas.txt"))