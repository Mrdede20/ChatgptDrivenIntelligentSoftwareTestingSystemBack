
import string

def to_base(num, b):
    digits = string.digits + string.ascii_uppercase
    if num < b:
        return digits[num]
    else:
        return to_base(num//b, b) + digits[num%b]
