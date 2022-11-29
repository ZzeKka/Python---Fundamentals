#sum that works for multiple data types
def new_sum(*items):
    if not items:
        return items
    output = items[0]
    for i in items[1:]:
        output += i
    return output

print(new_sum())
print(new_sum(10, 20, 30, 40))
print(new_sum('a', 'b', 'c', 'd'))
print(new_sum([10, 20, 30], [40, 50, 60], [70, 80]))