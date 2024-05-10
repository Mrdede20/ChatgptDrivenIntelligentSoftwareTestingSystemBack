
def coin_change_count(coins, total):
    if total == 0:
        return 1
    if total < 0 or not coins:
        return 0
    return coin_change_count(coins[:-1], total) + coin_change_count(coins, total - coins[-1])
