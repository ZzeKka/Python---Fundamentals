#orders strings is a list by number of vogals
def vogal_count(str):
    count = 0
    for s in str:
        if s in 'aeiou':
            count+=1
    return count

def vogal_sort(list):
    return sorted(list,key = vogal_count)

print(vogal_count('ola')) 
print(vogal_sort(['ola','ah','brobrobrobro','adeus']))
    
