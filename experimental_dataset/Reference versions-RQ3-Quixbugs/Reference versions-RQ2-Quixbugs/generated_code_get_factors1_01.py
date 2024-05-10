
import math

def get_factors(n):
    assert isinstance(n, int) and n > 0, "Input must be a positive integer"
    if n == 1:
        return []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return [i] + get_factors(n // i)
    return [n]

# Examples
print(get_factors(24)) # Output: [2, 2, 2, 3]
print(get_factors(13)) # Output: [13]
print(get_factors(100)) # Output: [2, 2, 5, 5]
