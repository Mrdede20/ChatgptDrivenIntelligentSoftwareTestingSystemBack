Here are the two Python programs to find the length of the longest common substring between two given strings s and t using dynamic programming:

Program 1: Using 2D Array

```
def longest_common_substring(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n+1) for _ in range(m+1)]
    max_len = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])
    return max_len
```

Program 2: Using Dictionary

```
def longest_common_substring(s, t):
    m, n = len(s), len(t)
    dp = {}
    max_len = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i, j] = dp.get((i-1, j-1), 0) + 1
                max_len = max(max_len, dp[i, j])
    return max_len
``` 

Both programs have the same method name `longest_common_substring()` and parameter types, so you can use either of them based on your preference.