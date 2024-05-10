
from math import sqrt
 
def get_factors(n):
    assert isinstance(n, int) and n > 0, "Input must be a positive integer"
    def get_factors_helper(n, i):
        if i > sqrt(n):
            return [n] if n > 1 else []
        if n % i == 0:
            return [i] + get_factors_helper(n // i, i)
        return get_factors_helper(n, i+1)
    return get_factors_helper(n, 2)
 
# Examples
print(get_factors(24)) # Output: [2, 2, 2, 3]
print(get_factors(13)) # Output: [13]
print(get_factors(100)) # Output: [2, 2, 5, 5]
