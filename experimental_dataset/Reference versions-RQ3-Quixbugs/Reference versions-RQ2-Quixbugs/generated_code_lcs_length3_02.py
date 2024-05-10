
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
