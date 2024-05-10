
def get_factors(n):
    factors = []
    if n == 1:
        return factors
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors
