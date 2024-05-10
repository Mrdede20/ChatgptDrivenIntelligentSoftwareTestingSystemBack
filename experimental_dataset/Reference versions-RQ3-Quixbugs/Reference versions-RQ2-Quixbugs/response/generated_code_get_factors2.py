Program 1:

Here is a solution using a recursive function to find the prime factors of an integer n using trial division:

```
def prime_factors(n):
    for i in range(2, n+1):
        if n % i == 0:
            return [i] + prime_factors(n // i)
    return []

n = int(input("Enter a number: "))
factors = prime_factors(n)
print("Prime factors:", factors)
```

Program 2:

Here is a slightly optimized version of the same function using memoization to store previously computed results, reducing the number of recursive calls:

```
def prime_factors(n, memo={}):
    if n in memo:
        return memo[n]
    for i in range(2, n+1):
        if n % i == 0:
            memo[n] = [i] + prime_factors(n // i, memo)
            return memo[n]
    memo[n] = []
    return memo[n]

n = int(input("Enter a number: "))
factors = prime_factors(n)
print("Prime factors:", factors)
```

Both programs take an integer parameter n and return its prime factors as a list, sorted in ascending order with repetition. The second program is slightly optimized by storing previously computed results using memoization to reduce the number of recursive calls.