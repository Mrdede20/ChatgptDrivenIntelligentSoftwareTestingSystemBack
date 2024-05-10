
def get_factors(n):
    factors = []
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            factors.append(i)
            n //= i
            factors.extend(get_factors(n))
            return factors
    factors.append(n)
    return factors
