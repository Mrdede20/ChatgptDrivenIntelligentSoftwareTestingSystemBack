
def possible_change(coins, total):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif len(coins) == 0:
        return 0
    else:
        return possible_change(coins[1:], total) + possible_change(coins, total-coins[0])
