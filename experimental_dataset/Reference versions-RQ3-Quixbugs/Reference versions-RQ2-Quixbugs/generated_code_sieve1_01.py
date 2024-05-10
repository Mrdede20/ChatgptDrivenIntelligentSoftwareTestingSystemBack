
def sieve_of_eratosthenes(max: int) -> List[int]:
    # Create an array of boolean values, indicating whether a number is prime
    is_prime = [True] * (max + 1)
    
    # Initialize variables
    p = 2
    result = []
    
    # Iterate until p^2 exceeds max
    while p * p <= max:
        # If p is prime, cross out all its multiples
        if is_prime[p]:
            for i in range(p * 2, max + 1, p):
                is_prime[i] = False
        # Move to the next prime number
        p += 1
    
    # Append all remaining prime numbers to the result
    for p in range(2, max + 1):
        if is_prime[p]:
            result.append(p)
    
    return result
