Here are two programs to achieve the same intention:

Program 1:

```
def longest_common_substring(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = {}
    max_len = 0
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[(i,j)] = 0
            elif s[i-1] == t[j-1]:
                dp[(i,j)] = dp[(i-1,j-1)] + 1
                max_len = max(max_len, dp[(i,j)])
            else:
                dp[(i,j)] = 0
                
    return max_len
```

Program 2:

```
def longest_common_substring(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    max_len = 0
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0
                
    return max_len
```

Both the programs have the same method name and parameter type. The only difference is in the implementation of the dp table. The first program uses a dictionary to store the dp values while the second program uses a 2D array. The time complexity of both the programs is O(len(s)*len(t)).