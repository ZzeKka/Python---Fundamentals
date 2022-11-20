def numbercloser(number,before,after):
    number_str = str(int(number))
    integer_number = int(number_str[(len(number_str) - before):])
    
    decimal_string = str(number - int(number))
    decimal_number = float(decimal_string[:2 + after])
    
    return integer_number + decimal_number
    
print(numbercloser(1234.5678,2,3))
  
