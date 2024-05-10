
def to_base(num, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num > 0:
        remainder = num % b
        result = digits[remainder] + result
        num //= b
    return result if result != "" else "0"
