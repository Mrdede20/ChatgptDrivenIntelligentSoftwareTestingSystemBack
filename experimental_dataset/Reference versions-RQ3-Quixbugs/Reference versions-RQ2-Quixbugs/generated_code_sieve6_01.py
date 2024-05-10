
def find_primes(max):
    primes = []
    for num in range(2, max+1):
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
