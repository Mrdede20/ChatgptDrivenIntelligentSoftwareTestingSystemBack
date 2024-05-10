Here are two programs that achieve the same purpose of calculating the GCD of two non-negative integers using the Euclidean algorithm:

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
        a, b = b, a % b
    return a
```

Both programs have the same function name `gcd` and take two non-negative integer parameters `a` and `b`. In program 1, the function uses recursion to implement the Euclidean algorithm. In program 2, the function uses a while loop to achieve the same result. In both cases, the function returns the GCD of `a` and `b`.