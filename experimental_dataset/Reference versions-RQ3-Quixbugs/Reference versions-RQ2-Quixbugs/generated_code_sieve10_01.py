
def sieve_of_eratosthenes(max):
    primes = []
    for num in range(2, max+1):
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
