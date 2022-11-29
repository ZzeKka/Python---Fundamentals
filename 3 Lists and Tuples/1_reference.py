"""    
List --- list = []

Tuple --- tuple = ()

List Comprehension --- Exemple: line.split(":")[0] for line in open('/etc/passwd')

range(0,3) --- 0,1,2

operator.itemgetter: --- itemgetter(1)('ABCD') -> 'B'
|down|
def itemgetter(*items):
   
    if len(items) == 1:
        
        item = items[0]
        
        def g(obj):
            return obj[item]
    else:
        def g(obj): 
            return tuple(obj[item] for item in items)
    return g  

---

collections.Counter

c = Counter(['eggs','ham'])

del c['eggs']

---

max([10,20,30]) -> 30
"""