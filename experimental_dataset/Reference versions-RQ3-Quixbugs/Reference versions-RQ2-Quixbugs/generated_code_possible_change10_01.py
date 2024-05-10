
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(coins) == 0 and total > 0:
        return 0
    return possible_change(coins[:-1], total) + possible_change(coins, total-coins[-1])
