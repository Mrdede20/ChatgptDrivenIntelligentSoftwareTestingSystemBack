
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
