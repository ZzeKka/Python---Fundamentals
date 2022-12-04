from collections import defaultdict

def word_lengths(filename):
    output = defaultdict(int)
    
    for one_line in open(filename):
        for one_word in one_line.split():
            output[len(one_word)] += 1
        return output
    
    