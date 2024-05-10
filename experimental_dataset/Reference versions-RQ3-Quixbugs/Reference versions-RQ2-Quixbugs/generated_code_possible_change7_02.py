
def coin_change_count(coins, total):
    return rec_coin(coins, total, {})

def rec_coin(coins, total, memo):
    if total == 0:
        return 1
    if total < 0 or not coins:
        return 0
    
    if (len(coins), total) in memo:
        return memo[(len(coins), total)]
    
    memo[(len(coins), total)] = rec_coin(coins[:-1], total, memo) + rec_coin(coins, total - coins[-1], memo)
    return memo[(len(coins), total)]
