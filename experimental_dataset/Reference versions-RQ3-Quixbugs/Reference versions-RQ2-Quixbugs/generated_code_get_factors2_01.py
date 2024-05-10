
def prime_factors(n):
    for i in range(2, n+1):
        if n % i == 0:
            return [i] + prime_factors(n // i)
    return []

n = int(input("Enter a number: "))
factors = prime_factors(n)
print("Prime factors:", factors)
