def transpose(word_list):
    return [' '.join(t) for t in (zip(*[s.split() for s in word_list]))]

print(transpose(['abc def ghi', 'jkl mno pqr', 'stu vwx yz'])) 