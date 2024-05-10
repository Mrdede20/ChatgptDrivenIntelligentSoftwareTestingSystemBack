
def sieve_of_eratosthenes(max:int) -> list:
    primes = []
    numbers = list(range(2, max+1))
    while numbers:
        p = numbers.pop(0)
        primes.append(p)
        numbers = [n for n in numbers if n % p != 0]
    return primes
