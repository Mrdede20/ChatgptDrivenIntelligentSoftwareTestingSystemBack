Here are two programs that achieve the same intention:

**Program 1:**
```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
```

**Program 2:**
```python
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)
```

Both programs are similar in that they use recursion to compute the GCD of 'a' and 'b'. The first program uses a base case where 'b' is equal to 0 and returns 'a' if 'b' is equal to 0. Otherwise, it calls the gcd function recursively with 'b' and 'a % b' as the new arguments. The second program has three base cases: if 'a' is equal to 0, it returns 'b'; if 'b' is equal to 0, it returns 'a'; and if 'a % b' is equal to 0, it returns 'b'. If none of the base cases are met, it calls the gcd function recursively with 'b' and 'a % b' as the new arguments.