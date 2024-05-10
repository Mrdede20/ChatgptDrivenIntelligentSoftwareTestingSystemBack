
def decimalToBase(num: int, b: int) -> str:
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    if num == 0:
        return '0'
    while num > 0:
        digit = digits[num % b]
        result = digit + result
        num = num // b
    return result
