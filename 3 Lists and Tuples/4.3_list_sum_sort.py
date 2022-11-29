#orders list of lists by sum of each list
def sum_sort(list):
    return sorted(list, key=sum)

print(sum_sort([[1,2,3],[],[0,1,2],[5]]))