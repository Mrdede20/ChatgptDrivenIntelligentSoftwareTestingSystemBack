
import string

def base_converter(num, b):
    if type(num) != int or type(b) != int or b < 2 or b > 36:
        return "Invalid input"
    
    alphabet = string.digits + string.ascii_uppercase
    result = ""
    
    while num > 0:
        num, remainder = divmod(num, b)
        result = alphabet[remainder] + result
    
    return result or '0'
