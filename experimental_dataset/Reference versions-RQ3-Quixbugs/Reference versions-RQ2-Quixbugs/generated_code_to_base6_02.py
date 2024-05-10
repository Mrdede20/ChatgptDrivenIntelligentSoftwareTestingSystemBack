
def to_base(num, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    if num == 0:
        return "0"
    while num > 0:
        rem = num % b
        result += digits[rem]
        num = num // b
    return result[::-1]
