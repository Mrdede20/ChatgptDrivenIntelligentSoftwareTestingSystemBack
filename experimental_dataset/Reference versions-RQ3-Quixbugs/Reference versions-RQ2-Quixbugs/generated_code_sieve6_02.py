
def find_primes(max):
    primes = []
    candidates = [True] * (max+1)
    for num in range(2, max+1):
        if candidates[num]:
            primes.append(num)
            for multiple in range(num*num, max+1, num):
                candidates[multiple] = False
    return primes
