Here are two possible implementations of the Sieve of Eratosthenes algorithm in Python:

**Implementation 1 using array:**

```python
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
```

**Implementation 2 using set:**

```python
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
```