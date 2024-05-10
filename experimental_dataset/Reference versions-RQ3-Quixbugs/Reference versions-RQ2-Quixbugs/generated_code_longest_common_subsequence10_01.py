
def longest_common_subsequence(s1, s2):
    if not s1 or not s2:
        return ""
    elif s1[0] == s2[0]:
        return s1[0] + longest_common_subsequence(s1[1:], s2[1:])
    else:
        lcs1 = longest_common_subsequence(s1[1:], s2)
        lcs2 = longest_common_subsequence(s1, s2[1:])
        return lcs1 if len(lcs1) > len(lcs2) else lcs2
