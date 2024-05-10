
import string

def to_base(num, b):
    if num < 0:
        return '-' + to_base(-num, b)
    alphabet = string.digits + string.ascii_uppercase
    result = ''
    while num:
        num, rem = divmod(num, b)
        result = alphabet[rem] + result
    return result or '0'
