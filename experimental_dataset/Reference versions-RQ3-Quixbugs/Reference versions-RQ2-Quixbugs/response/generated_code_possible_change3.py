Program 1:

```
def count_change(total, denominations):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if not denominations:
        return 0
    return count_change(total - denominations[0], denominations) + count_change(total, denominations[1:])
```

Program 2:

```
def count_change(total, denominations):
    if total == 0:
        return 1
    if total < 0 or not denominations:
        return 0
    return count_change(total - denominations[0], denominations) + count_change(total, denominations[1:])
```

Both programs take in a total value and a list of coin denominations, and recursively computes the number of ways to change the total value using the given denominations. 

The first program checks for an empty denominations list before proceeding with the recursive call. The second program combines the second and third if statements into one by using an "or" condition. 

Both programs should produce the same result and achieve the same intention.