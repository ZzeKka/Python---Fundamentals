from operator import itemgetter


PEOPLE = [
{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'},
{'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}
]

def order_names(people):
    return sorted(people,key=itemgetter('last','first'))

print(order_names(PEOPLE))
        
