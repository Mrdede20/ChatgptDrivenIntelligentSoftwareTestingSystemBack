
from collections import defaultdict

def knapsack(capacity, items):
    dp = defaultdict(int)
    for i in range(len(items)):
        for w in range(capacity+1):
            if items[i][0] <= w:
                dp[(i, w)] = max(dp[(i-1, w)], dp[(i-1, w-items[i][0])] + items[i][1])
            else:
                dp[(i, w)] = dp[(i-1, w)]
    return dp[(len(items)-1, capacity)]
