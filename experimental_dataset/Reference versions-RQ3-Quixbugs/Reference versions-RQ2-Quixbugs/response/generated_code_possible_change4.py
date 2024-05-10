Program 1:

```
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0 or len(coins) == 0:
        return 0
    return possible_change(coins[1:], total) + possible_change(coins, total - coins[0])
```

Program 2:

```
def possible_change(coins, total):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif len(coins) == 0:
        return 0
    else:
        return possible_change(coins[1:], total) + possible_change(coins, total-coins[0])
```

Both of these programs achieve the intention of calculating the number of distinct ways to make change that adds up to the given "total" using only the coins in the given list of denominations. They both use recursion to repeatedly call the function with a smaller subset of the denominations and a smaller total until they reach the base case where the total is either 0 or negative.