from decimal import Decimal

def decimal_sum(str1, str2):
    x = Decimal(str1)
    y = Decimal(str2)
    print(x + y)
    
decimal_sum('0.1','0.2')