
def count_change(total, coins):
    memo = {}
    
    def count_helper(total, coins):
        if (total, len(coins)) in memo:
            return memo[(total, len(coins))]
        if total == 0:
            return 1
        if total < 0 or len(coins) == 0:
            return 0
        result = count_helper(total - coins[0], coins) + count_helper(total, coins[1:])
        memo[(total, len(coins))] = result
        return result
    
    return count_helper(total, coins)
