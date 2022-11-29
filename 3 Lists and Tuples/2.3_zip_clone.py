#does the same as zip()
def zip_clone(item1,item2):
    output = []
    index = 0
    for n1 in item1:
        output.append((n1,))    
    for n2 in item2:
        output[index] += (n2,)
        index += 1
    return output

def zip_clone_solution(*args):
    return [tuple(a[i] for a in args) for i in range(len(min(args,key = len)))]
    
        
print(zip_clone_solution([1,2,3],'abc'))

#guide for solution
#1st min(args, key=len) -> [1,2,3] compares the lest len iterable
#2nd len is 3 because it's the minium so it cycles 3 times
#each type in ads a tuple to the list 