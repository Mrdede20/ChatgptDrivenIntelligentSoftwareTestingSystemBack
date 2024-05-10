Program 1:

```python
def coin_change(coins, total):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif len(coins) == 0:
        return 0
    else:
        return coin_change(coins[:-1], total) + coin_change(coins, total - coins[-1])
```

Program 2:

```python
def coin_change(coins, total):
    def count(coins, m, total):
        if total == 0:
            return 1
        if total < 0:
            return 0
        if m <= 0 and total >= 1:
            return 0
        return count(coins, m-1, total) + count(coins, m, total - coins[m-1])
    return count(coins, len(coins), total)
```

Both programs use the same method name `coin_change` and the same parameter type of a list of coin denominations (`coins`) and a total value to make change for (`total`). 

The first program uses a straightforward recursive approach, where at each level of the recursion we consider using either the last coin denomination (by making a call to the function with the updated `total` and the original list except for the last coin using `coins[:-1]`) or we consider not using the last coin denomination (by making a call to the function with the original `total` and the original list except for the last coin using `coins`).

The second program uses a similar recursive approach, but with an inner helper function `count` that takes an additional parameter `m` that represents the last index of the list `coins` that can be used to make change. This makes the function more efficient than the first program by reducing the size of the list being considered at each level of recursion. The helper function is then called with `m` set to the length of `coins`, and the function returns the total count from the helper function.