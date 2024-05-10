
def prime_factors(n, factor=2):
    if n == 1:
        return []
    if n % factor == 0:
        return [factor] + prime_factors(n//factor, factor)
    else:
        return prime_factors(n, factor+1)
