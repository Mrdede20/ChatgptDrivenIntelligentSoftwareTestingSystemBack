
def sieve_of_eratosthenes(max):
    primes = []
    is_prime = [True] * (max + 1)
    for num in range(2, max + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, max + 1, num):
                is_prime[multiple] = False
    return primes
