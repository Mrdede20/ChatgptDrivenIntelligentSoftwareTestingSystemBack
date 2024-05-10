Program 1:

```python
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(coins) == 0 and total > 0:
        return 0
    return possible_change(coins[:-1], total) + possible_change(coins, total-coins[-1])
```

Program 2:

```python
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if not coins and total > 0:
        return 0
    return possible_change(coins[1:], total) + possible_change(coins, total-coins[0])
```

Both programs achieve the same result and use the same method name and parameter type. The only difference is in the way they handle the `coins` list. Program 1 uses slicing to remove the last coin from the list, while program 2 uses slicing to remove the first coin from the list.