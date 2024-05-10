
def coin_change(coins, total):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif len(coins) == 0:
        return 0
    else:
        return coin_change(coins[:-1], total) + coin_change(coins, total - coins[-1])
