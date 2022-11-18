#function that sortes a string in unicode order
def strsort(str):
    return ''.join(sorted(str))
    
print(strsort('acdeab'))