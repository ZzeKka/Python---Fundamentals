def word_per_line(filename):
    output = []
    
    for n, line in enumerate(open(filename)):
        words = line.split()
        
        output.append(words[n])
    
    return ' '.join(output)
            
print(word_per_line("boas.txt"))