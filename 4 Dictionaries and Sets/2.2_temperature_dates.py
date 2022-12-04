

from datetime import datetime, timedelta

METEREOLOGY = {
    '2020-08-16': 30,
    '2020-08-17': 32,
    '2020-08-18': 32,
}

def get_temperature():
    while True:
        
        date = input("plz enter a date: ").strip()
        
        if len(date) != 10 or date.count('-') != 2 or date not in METEREOLOGY: 
            print("Wrong format")
            continue
        
        try:
            today = datetime.fromisoformat(date).date()
        except ValueError as e:
            print("invalid")
            continue
        yesterday = str(today - timedelta(1))
        tomorrow = str(today + timedelta(1))
        
        print(f"yesterday -> {yesterday} : {METEREOLOGY.get(yesterday, 'no data available')} Cº")
        print(f"TODAY -> {date} : {METEREOLOGY.get(date)} Cº")
        print(f"tomorrow -> {tomorrow} : {METEREOLOGY.get(tomorrow, 'no data available')} Cº")
            
get_temperature()

    
    