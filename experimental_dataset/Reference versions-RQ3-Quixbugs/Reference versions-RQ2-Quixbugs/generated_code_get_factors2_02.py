
def prime_factors(n, memo={}):
    if n in memo:
        return memo[n]
    for i in range(2, n+1):
        if n % i == 0:
            memo[n] = [i] + prime_factors(n // i, memo)
            return memo[n]
    memo[n] = []
    return memo[n]

n = int(input("Enter a number: "))
factors = prime_factors(n)
print("Prime factors:", factors)
