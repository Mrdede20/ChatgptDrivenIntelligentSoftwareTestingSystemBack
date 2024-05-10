
from collections import Counter

def longest_common_substring(s, t):
    dp = Counter()
    max_len = 0
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[(i,j)] = dp[(i-1,j-1)] + 1
                max_len = max(max_len, dp[(i,j)])
    return max_len if dp else 0
