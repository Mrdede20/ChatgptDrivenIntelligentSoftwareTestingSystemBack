
import string

def to_base(num, b):
    if num == 0:
        return "0"
    elif num < 0:
        return "-" + to_base(-1*num, b)
    else:
        result = ""
        alphabet = string.digits + string.ascii_uppercase
        while num > 0:
            rem = num % b
            result = alphabet[rem] + result
            num = num // b
        return result
