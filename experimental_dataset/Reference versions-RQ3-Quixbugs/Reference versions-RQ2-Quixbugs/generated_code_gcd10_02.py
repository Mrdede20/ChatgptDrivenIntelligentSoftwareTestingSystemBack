
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)
