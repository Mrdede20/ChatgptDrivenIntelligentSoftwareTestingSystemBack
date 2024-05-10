
def lcs_length(s: str, t: str) -> int:
    dp = {}
    max_len = 0
    for i in range(len(s)):
        for j in range(len(t)):
            if i == 0 or j == 0:
                dp[(i,j)] = 0
            elif s[i-1] == t[j-1]:
                dp[(i,j)] = dp[(i-1, j-1)] + 1
                max_len = max(max_len, dp[(i,j)])
            else:
                dp[(i,j)] = 0
    return max_len
