#combines dictionaries (solution)
def combine_dicts(*args):
    
    output = {}
    
    for d in args:
        for key,value in d.items():
            print((key,value))
            if key in output:
                try:
                    output[key].append(value)
                except AttributeError:
                    output[key] = [output[key],value]
            else:
                output[key] = value
    return output


print(combine_dicts({'ola':22,'adeus':12},{'forass':2,'adeus':1}))

