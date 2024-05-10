
from collections import Counter

def longest_common_substring(s, t):
    dp = Counter()
    max_len = 0
    for i, s_char in enumerate(s):
        for j, t_char in enumerate(t):
            if s_char == t_char:
                dp[(i,j)] = dp[(i-1,j-1)] + 1
                max_len = max(max_len, dp[(i,j)])
    return max_len if dp else 0
