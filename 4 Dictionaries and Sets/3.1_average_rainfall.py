dict = {}

def rainfall():
    while True:
        city = input("Enter a City name: ").strip()
        if city != '':
            rainfall = int(input("Enter rainfall level: ").strip())
            dict[city] = dict.get(rainfall,0) + int(rainfall) 
                 
        else:
            rainfall_sum = 0
            for item, value in dict.items():
                print(f"{item}:{value}")
                rainfall_sum += value
            print(f"average: {rainfall_sum/len(dict.keys())}")
            break

rainfall()