
def gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        temp = b
        b = a % b
        a = temp
    
    return a
