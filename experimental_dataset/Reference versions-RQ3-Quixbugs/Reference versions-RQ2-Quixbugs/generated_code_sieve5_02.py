
def sieve_of_eratosthenes(max:int) -> list:
    primes = []
    is_prime = [True] * (max+1)
    for n in range(2, max+1):
        if is_prime[n]:
            primes.append(n)
            for multiple in range(n*n, max+1, n):
                is_prime[multiple] = False
    return primes
