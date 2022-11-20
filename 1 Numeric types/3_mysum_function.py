#implementing sum function with dynamic arguments

#Sum dinamicly placed numbers
def mysum(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

#Sum function with a starting point argument
def mysum_2(numbers,start = 0):
    sum = start
    for n in numbers:
        sum += n
    return sum 

#average beetween an array of numbers
def average(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum / len(numbers)

#return a tuple with information related to a string
def word_info(string):
    data = ()
    words = string.split()
    min_len = float('inf')
    max_len = 0
    all_len = 0
    for word in words:
        if(len(word) < min_len):
            min_len = len(word)
        if(len(word) > max_len):
            max_len = len(word)
        all_len += len(word)
    data = (min_len, max_len, all_len/len(words))
    return data

#takes a list of data types and sums the ones that are possible to sum
def objectsum(list):
    sum = 0
    for n in list:
        try:
            sum += int(n)
        except: 
            continue
    return sum    
    
            
        
        
    
    


#print(mysum(1,2,3))

#print(mysum_2([1,2,3]))
#print(mysum_2([1,2,3],3))

#print(average([1,2,3]))
    
#print(word_info("este programa   funciona"))

print(objectsum([1,"2","abc"]))