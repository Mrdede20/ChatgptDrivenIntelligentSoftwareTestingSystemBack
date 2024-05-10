Here are two programs that achieve the same intention using the same method name and parameter type:

Program 1: Using Recursive approach

```python
def longest_common_subsequence(a, b):
    if len(a) == 0 or len(b) == 0:
        return ""
    elif a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b[1:])
    else:
        subseq1 = longest_common_subsequence(a, b[1:])
        subseq2 = longest_common_subsequence(a[1:], b)
        return subseq1 if len(subseq1) > len(subseq2) else subseq2
```

Program 2: Using Dynamic Programming approach

```python
def longest_common_subsequence(a, b):
    m = len(a)
    n = len(b)
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    result = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            result = a[i-1] + result
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    return result
```

Both programs take two string inputs 'a' and 'b' and return the longest common subsequence between them. The first program uses a recursive approach while the second program uses dynamic programming. The dynamic programming approach is generally more efficient than the recursive approach, especially for longer strings.