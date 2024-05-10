
def count_change(coins, total, memo={}):
    if total == 0:
        return 1
    elif total < 0 or not coins:
        return 0
    elif (len(coins), total) in memo:
        return memo[(len(coins), total)]
    else:
        memo[(len(coins), total)] = count_change(coins[:-1], total, memo) + count_change(coins, total-coins[-1], memo)
        return memo[(len(coins), total)]
