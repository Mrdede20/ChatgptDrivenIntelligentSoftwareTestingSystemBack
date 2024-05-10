
import math

def prime_factors(n):
    if n == 1:
        return []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return [i] + prime_factors(n // i)
    return [n]
