
def longest_common_subsequence(s1, s2):
    memo = {}
    def lcs_helper(i, j):
        if i >= len(s1) or j >= len(s2):
            return ""
        elif (i, j) in memo:
            return memo[(i, j)]
        elif s1[i] == s2[j]:
            result = s1[i] + lcs_helper(i+1, j+1)
        else:
            lcs1 = lcs_helper(i+1, j)
            lcs2 = lcs_helper(i, j+1)
            result = lcs1 if len(lcs1) > len(lcs2) else lcs2
        memo[(i, j)] = result
        return result
    return lcs_helper(0, 0)
