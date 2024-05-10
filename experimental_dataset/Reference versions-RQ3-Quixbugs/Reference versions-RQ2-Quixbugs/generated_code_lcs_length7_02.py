
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
