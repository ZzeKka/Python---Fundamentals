dict = {}

def rainfall():
    while True:
        city = input("Enter a City name: ").strip()
        if city != '':
            rainfall = int(input("Enter rainfall level: ").strip())
            dict[city] = dict.get(rainfall,0) + int(rainfall) 
                 
        else:
            for item, value in dict.items():
                print(f"{item}:{value}")
            break

rainfall()




    