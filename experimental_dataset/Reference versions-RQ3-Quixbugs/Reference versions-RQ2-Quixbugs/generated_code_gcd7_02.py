
def gcd(a: int, b: int) -> int:
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a
