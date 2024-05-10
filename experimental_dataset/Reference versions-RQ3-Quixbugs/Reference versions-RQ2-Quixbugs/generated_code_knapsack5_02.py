
def knapsack(capacity, items):
    def helper(i, j):
        if i < 0 or j == 0:
            return 0
        weight, value = items[i]
        if weight > j:
            return helper(i-1, j)
        else:
            return max(helper(i-1, j), helper(i-1, j-weight) + value)

    return helper(len(items)-1, capacity)
