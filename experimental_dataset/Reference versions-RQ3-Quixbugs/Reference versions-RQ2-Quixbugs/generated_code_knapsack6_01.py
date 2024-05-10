
def knapsack_recursive_memoization(weights, values, capacity):
    memo = [[None] * (capacity + 1) for _ in range(len(weights))]
    
    def knapsack_helper(i, remaining_capacity):
        if i < 0 or remaining_capacity <= 0:
            return 0
        if memo[i][remaining_capacity] is not None:
            return memo[i][remaining_capacity]
        include = values[i] + knapsack_helper(i - 1, remaining_capacity - weights[i])
        exclude = knapsack_helper(i - 1, remaining_capacity)
        result = max(include, exclude)
        memo[i][remaining_capacity] = result
        return result
    
    return knapsack_helper(len(weights) - 1, capacity)
