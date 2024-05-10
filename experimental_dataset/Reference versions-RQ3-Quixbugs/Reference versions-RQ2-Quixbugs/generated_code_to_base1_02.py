
def to_base(num, b):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while num > 0:
        remainder = num % b
        num //= b
        result.append(alphabet[remainder])
    return ''.join(result[::-1])
