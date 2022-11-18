#returns the longest word in file
def longest_word(filename):
    

    output = ''
    
    for line in open(filename):
        for word in line.split():
            if word.isalpha() and len(word) > len(output):
                output = word
            else:
                continue
    return output

print(longest_word("boas.txt"))