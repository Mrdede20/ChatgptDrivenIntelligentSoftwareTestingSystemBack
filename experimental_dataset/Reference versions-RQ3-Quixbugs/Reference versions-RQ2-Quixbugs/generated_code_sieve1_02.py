
def sieve_of_eratosthenes(max: int) -> List[int]:
    # Create a set of integers from 2 up to max
    numbers = set(range(2, max + 1))
    result = []
    
    # Iterate until numbers is empty
    while numbers:
        # Get the smallest number in the set (which is a prime number)
        p = min(numbers)
        
        # Add p to the result and remove all its multiples from the set
        result.append(p)
        multiples = set(range(p * 2, max + 1, p))
        numbers -= multiples
    
    return result
