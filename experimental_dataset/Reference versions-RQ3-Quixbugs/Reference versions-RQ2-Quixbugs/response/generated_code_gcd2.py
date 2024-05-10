Here are two programs in Python that achieve the intention:

Program 1:

```
def gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        temp = b
        b = a % b
        a = temp
    
    return a
```

Program 2:

```
def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)
```

Both programs achieve the same goal of finding the GCD of two non-negative integers using the Euclidean Algorithm recursively. The first program uses a while loop to iterate until the smaller number becomes 0 and returns the larger number, which is the GCD. The second program uses recursive function calls to reduce the problem to smaller subproblems until the base case of b being 0 is reached, at which point it returns a, the larger number, which is the GCD.