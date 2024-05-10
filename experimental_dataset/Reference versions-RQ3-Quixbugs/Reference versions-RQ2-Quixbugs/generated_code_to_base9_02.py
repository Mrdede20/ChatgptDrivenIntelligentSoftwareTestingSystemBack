
def to_base(num, b):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base_b_num = ""
    while num != 0:
        rem = num % b
        base_b_num = alphabet[rem] + base_b_num
        num //= b
    return "0" if base_b_num == "" else base_b_num
