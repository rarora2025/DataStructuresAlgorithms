import checkmycode

def binary(val, binary_str):
    if(val == 0):
        return binary_str
    
    return binary(val//2, str(val%2) + binary_str)


def binary_converter(num):
    return binary(num, "")
