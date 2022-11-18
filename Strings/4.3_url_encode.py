import string

def url_encode(text):
    
    safe_chars = string.ascii_letters + string.digits
    output = []
    
    for one_character in text:
        if one_character in safe_chars:
            output.append(one_character)
        else:
            output.append(hex(ord(one_character)).replace('0x','%'))
    return ''.join(output)