Program 1:

```
from collections import Counter

def lcs_length(s, t):
    m, n = len(s), len(t)
    dp = Counter()
    max_len = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[(i, j)] = dp[(i-1, j-1)] + 1
                max_len = max(max_len, dp[(i, j)])
    return max_len
```

Program 2:

```
from collections import Counter

def lcs_length(s, t):
    m, n = len(s), len(t)
    dp = Counter()
    max_len = 0
    for i in range(m):
        for j in range(n):
            if s[i] == t[j]:
                if (i-1, j-1) in dp:
                    dp[(i,j)] = dp[(i-1,j-1)] + 1
                else:
                    dp[(i,j)] = 1
                max_len = max(max_len, dp[(i,j)])
    return max_len
```

Both programs use the dynamic programming approach to calculate the length of the longest common substring. They iterate over the characters of the two strings and store the length of the common substring up to that position in a `Counter` object `dp`. They also maintain a variable `max_len` to store the maximum common substring length. Program 1 iterates over indices ranging from 1 to `m` and 1 to `n`, while Program 2 iterates over indices ranging from 0 to `m-1` and 0 to `n-1`. The difference is in the way the indices are handled while updating `dp`.