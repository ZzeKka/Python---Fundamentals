def pl_sentence(phrase):
    translation = []
    for word in phrase.split():
        if(word[0] in 'aeiou'):
            translation.append(f"{word}way")
        else:
            translation.append(f" {word[1:]}{word[0]}ay")
    print(' '.join(translation))

pl_sentence('this is a test translation')
#output: histay isway away estay ranslationtay