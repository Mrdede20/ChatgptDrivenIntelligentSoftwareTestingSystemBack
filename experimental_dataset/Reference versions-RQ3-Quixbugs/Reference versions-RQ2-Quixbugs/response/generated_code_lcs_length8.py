Program 1:

```python
from collections import Counter

def longest_common_substring(s, t):
    m, n = len(s), len(t)
    dp = Counter()
    max_len = 0
    for i in range(m):
        for j in range(n):
            if s[i] == t[j]:
                dp[i,j] = dp[i-1,j-1]+1
                max_len = max(max_len,dp[i,j])
    return max_len
```

Program 2:

```python
from collections import Counter

def longest_common_substring(s, t):
    m, n = len(s), len(t)
    dp = Counter()
    max_len = 0
    for i in range(m):
        for j in range(n):
            if s[i] == t[j]:
                if i == 0 or j == 0:
                    dp[i,j] = 1
                else:
                    dp[i,j] = dp[i-1,j-1]+1
                max_len = max(max_len,dp[i,j])
    return max_len
```

Both programs use the same method name and parameter type to find the length of the longest common substring between two input strings `s` and `t`. The difference between the two programs is in the way the DP table is initialized. Program 1 initializes the DP table with a `Counter` object, whereas Program 2 initializes the table with zeros and sets the value of dp[i,j] = 1 if i or j is 0.