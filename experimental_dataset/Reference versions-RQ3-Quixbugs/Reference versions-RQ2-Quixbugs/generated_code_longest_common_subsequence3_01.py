
def longest_common_subsequence(a, b):
    if len(a) == 0 or len(b) == 0:
        return ""
    elif a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b[1:])
    else:
        sub1 = longest_common_subsequence(a[1:], b)
        sub2 = longest_common_subsequence(a, b[1:])
        sub3 = longest_common_subsequence(a[1:], b[1:])
        longest_sub = max(sub1, sub2, sub3, key=len)
        return longest_sub
