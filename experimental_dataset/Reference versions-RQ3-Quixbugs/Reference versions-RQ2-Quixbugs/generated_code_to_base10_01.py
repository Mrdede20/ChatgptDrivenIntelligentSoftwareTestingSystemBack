
import string

def to_base(num, b):
    digits = string.digits + string.ascii_uppercase
    result = ""
    while num:
        num, rem = divmod(num, b)
        result += digits[rem]
    return result[::-1] if result else digits[0]
