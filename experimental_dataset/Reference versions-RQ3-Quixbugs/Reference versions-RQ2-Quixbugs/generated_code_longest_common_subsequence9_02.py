
def longest_common_subsequence(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return ""
    elif str1[0] == str2[0]:
        return str1[0] + longest_common_subsequence(str1[1:], str2[1:])
    else:
        lcs1 = longest_common_subsequence(str1[1:], str2)
        lcs2 = longest_common_subsequence(str1, str2[1:])
        return max(lcs1, lcs2, key=len)
