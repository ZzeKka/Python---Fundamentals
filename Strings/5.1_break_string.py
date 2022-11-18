#break lines apart, and sorts word and divides them with ','
def sorted_words(str):
    return ','.join(sorted(str.split()))

print(sorted_words("Tom Dick Harry"))

