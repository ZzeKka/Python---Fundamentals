#print tuples in a clean way
from operator import itemgetter

PEOPLE = [('Donald', 'Trump', 7.85),
('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)]

def print_tuple(list):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    
    for person in sorted(list, key = itemgetter(2)):
        output.append(template.format(*person))
    print('\n'.join(output))
    

print_tuple(PEOPLE)
 