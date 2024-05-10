Here are the two programs:

Program 1:

```python
def longest_common_substring_length(s: str, t: str) -> int:
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_length = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])
    return max_length
```

Program 2:

```python
def longest_common_substring_length(s: str, t: str) -> int:
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_length = 0
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                max_length = max(max_length, dp[i+1][j+1])
    return max_length
```

Both programs take in two strings "s" and "t" and return the length of the longest common substring between them. They make use of dynamic programming and store the lengths of common substrings in a 2D-array. The first program accesses the strings using indices, while the second program uses range-based iteration.