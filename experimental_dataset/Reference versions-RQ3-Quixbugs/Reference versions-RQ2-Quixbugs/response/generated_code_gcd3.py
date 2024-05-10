Program 1:

```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
```

Program 2:

```python
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)
```

Both of these programs implement the Greatest Common Divisor algorithm using recursion. They take two non-negative integers a and b as input and return the greatest integer that evenly divides both a and b. The function calls itself with the values (a % b) and b until b is equal to 0. At this point, the function returns the current value of a, which is the GCD of the original a and b. The second program also takes care of the scenario when either a or b is 0, in which case it just returns the other number as the GCD.