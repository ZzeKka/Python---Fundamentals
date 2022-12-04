
from datetime import datetime, timedelta, date

BIRTH = {
    'Ana' : '1998-07-15',
    'Rafa' : '1992-01-04',
    'Gaia' : '1920-12-30'
}

def family_birth():
    while True:
        name = input("Whos the family member you wanna know the birth off? ").strip()
        if name in BIRTH:
            birth_date = BIRTH.get(name,'Error')
            today = date.today()
            try:
                birth_date = datetime.fromisoformat(birth_date).date()
            except ValueError as e:
                print("invalid")
                continue
            age = today.year - birth_date.year - ((today.month,today.day) > (birth_date.month,birth_date.day))
            print(f"{name} is {age} years old")
            
            
            break
        else:
            print("enter a correct name")
            continue

#worse than mine
def birth_solution() : 
    while True:
        name = input("Whos the family member you wanna know the birth off? ").strip()

        if not name: 
            break
        
        today = date.today()
        
        if name in BIRTH:
            print(f"{name} is {(today - BIRTH[name]).days}")  # type: ignore
        
family_birth()