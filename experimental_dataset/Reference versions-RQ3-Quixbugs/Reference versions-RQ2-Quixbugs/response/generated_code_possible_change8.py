Sure, here are two possible implementations:

Implementation 1:

```python
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(coins) == 0:
        return 0
    return (possible_change(coins, total-coins[0]) 
            + possible_change(coins[1:], total))
```

This implementation checks if the `coins` list is empty and returns 0 if it is. It also takes the first coin in the list and uses it in one of the recursive calls, while excluding it from the other call by slicing the list.


Implementation 2:

```python
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0 or len(coins) == 0:
        return 0
    return (possible_change(coins[:-1], total) 
            + possible_change(coins, total-coins[-1]))
```

This implementation is similar to the first one, but it excludes the last coin in the list in the first recursive call, and uses it in the second recursive call. This way, it performs a similar operation, but with a different subset of the `coins` list.