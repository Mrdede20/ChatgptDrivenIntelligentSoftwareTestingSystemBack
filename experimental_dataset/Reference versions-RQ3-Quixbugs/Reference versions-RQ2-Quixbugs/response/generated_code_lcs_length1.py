Sure, here are two implementations of the same function using dynamic programming approach:

Implementation 1:

```
def longest_common_substring_length(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])
    
    return max_length
```

Implementation 2:

```
def longest_common_substring_length(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = {}
    max_length = 0
    
    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        if (i, j) in dp:
            return dp[(i, j)]
        
        if s[i-1] == t[j-1]:
            dp[(i, j)] = helper(i-1, j-1) + 1
            max_length = max(max_length, dp[(i, j)])
        else:
            dp[(i, j)] = 0
        
        dp[(i, j)] = max(dp[(i, j)], helper(i-1, j), helper(i, j-1))
        max_length = max(max_length, dp[(i, j)])
        return dp[(i, j)]
    
    helper(m, n)
    return max_length
```

Both implementations use dynamic programming approach to find the length of the longest common substring by computing the length of the longest common suffix obtained by checking the current character of each string, and then comparing it to the length of the longest common suffix obtained by excluding either s[i] or t[j]. Finally, the function returns the maximum value of the dictionary of calculated values of the longest common substring of s and t.