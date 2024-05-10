
def to_base(num, b):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return "0"
    base_b_num = ""
    while num != 0:
        rem = num % b
        base_b_num = alphabet[rem] + base_b_num
        num //= b
    return base_b_num
