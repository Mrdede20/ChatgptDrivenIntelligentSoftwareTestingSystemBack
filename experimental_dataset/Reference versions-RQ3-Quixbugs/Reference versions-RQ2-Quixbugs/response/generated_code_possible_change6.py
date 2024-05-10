Sure, here are two programs that achieve the same goal:

**Program 1**
```python
def possible_change(total, coins):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(coins) == 0:
        return 0
    return possible_change(total - coins[0], coins) + possible_change(total, coins[1:])
```
This program uses recursion and the function `possible_change` takes in two parameters: `total`, which is the total amount of change that needs to be made, and `coins`, which is a list of available coin denominations.

**Program 2**
```python
def possible_change(total, coins):
    possibilities = [0] * (total + 1)
    possibilities[0] = 1
    for coin in coins:
        for i in range(coin, total + 1):
            possibilities[i] += possibilities[i - coin]
    return possibilities[total]
```
This program uses dynamic programming and the function `possible_change` takes in two parameters: `total`, which is the total amount of change that needs to be made, and `coins`, which is a list of available coin denominations.

Both programs return the number of distinct ways to make change using coins of the given denominations. The first program uses recursion to consider all possible combinations of coins, while the second program uses dynamic programming to build up a table of solutions from smaller subproblems. The second program is generally more efficient, especially for larger values of `total` and larger lists of `coins`.