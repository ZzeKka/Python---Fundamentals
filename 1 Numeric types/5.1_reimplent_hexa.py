#This function will turn hexa number to decimal withiout using int()
decimal = 0
hexa = ""
while not hexa.isdigit():
    hexa = input("Write number: ")
for index,value in enumerate(reversed(hexa)):
    decimal += ((16 ** index) * (ord(value) - 48))
print(decimal)    
