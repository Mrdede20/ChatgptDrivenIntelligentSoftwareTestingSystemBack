
import string

def to_base(num, b):
    if not isinstance(b, int) or b < 2 or b > 36:
        raise ValueError("Base must be an integer between 2 and 36")
    if not isinstance(num, int) or num < 0:
        raise ValueError("Number must be a positive integer")
    alphabet = string.digits + string.ascii_uppercase
    result = ''
    while num > 0:
        num, remainder = divmod(num, b)
        result += alphabet[remainder]
    return result[::-1] if result else '0'
