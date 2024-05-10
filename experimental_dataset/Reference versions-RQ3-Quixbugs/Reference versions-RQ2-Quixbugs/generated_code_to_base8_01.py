
def to_base(num: int, b: int) -> str:
    if num < 0 or b < 2:
        raise ValueError("Invalid input: num must be non-negative and b must be greater than or equal to 2.")
    result = ""
    alphabet = "0123456789ABCDEF"
    while num > 0:
        remainder = num % b
        result = alphabet[remainder] + result
        num //= b
    return result
