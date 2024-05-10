Program 1:

```
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
```
Program 2:

```
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
```

Both of these codes implement the Euclidean algorithm to find the GCD of two non-negative integers. The first program uses recursion and the second program uses a loop.