#same as exercise 6, but using namedtuple


import operator
from collections import namedtuple

Person = namedtuple('Person', ['first', 'last', 'distance'])


PEOPLE = [Person('Donald', 'Trump', 7.85),
          Person('Vladimir', 'Putin', 3.626),
          Person('Jinping', 'Xi', 10.603)]



output = []
template = '{last:10} {first:10} {distance:5.2f}'
for person in sorted(PEOPLE, key=operator.attrgetter('last', 'first')):
    output.append(template.format(**(person._asdict())))
print('\n'.join(output))





