
def sieve_of_eratosthenes(upper_bound):
    primes = []
    is_prime = [False, False] + [True] * (upper_bound - 1)
    
    for num in range(2, upper_bound + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, upper_bound + 1, num):
                is_prime[multiple] = False
    
    return primes
