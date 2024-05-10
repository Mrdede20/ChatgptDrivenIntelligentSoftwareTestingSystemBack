
def longest_common_substring_length(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = {}
    max_length = 0
    
    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        if (i, j) in dp:
            return dp[(i, j)]
        
        if s[i-1] == t[j-1]:
            dp[(i, j)] = helper(i-1, j-1) + 1
            max_length = max(max_length, dp[(i, j)])
        else:
            dp[(i, j)] = 0
        
        dp[(i, j)] = max(dp[(i, j)], helper(i-1, j), helper(i, j-1))
        max_length = max(max_length, dp[(i, j)])
        return dp[(i, j)]
    
    helper(m, n)
    return max_length
