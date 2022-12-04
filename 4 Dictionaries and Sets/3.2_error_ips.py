from collections import defaultdict

def error_ip_addresses(filename):
    output = defaultdict(list)
    
    for one_line in open(filename):
        fields = one_line.split()
        ip_address = fields[0]
        response_code = fields[0]
        output[response_code].append(ip_address)
    return output

