
def to_base(num: int, b: int) -> str:
    if num < 0 or b < 2:
        raise ValueError("Invalid input: num must be non-negative and b must be greater than or equal to 2.")
    result = ""
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while num > 0:
        remainder = num % b
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = alphabet[remainder - 10] + result
        num //= b
    return result
