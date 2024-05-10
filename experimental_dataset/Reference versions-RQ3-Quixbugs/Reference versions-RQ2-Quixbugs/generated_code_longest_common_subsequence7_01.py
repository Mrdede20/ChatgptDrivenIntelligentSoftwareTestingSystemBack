
def longest_common_subsequence(a, b):
    if len(a) == 0 or len(b) == 0:
        return ""
    elif a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b[1:])
    else:
        subseq1 = longest_common_subsequence(a, b[1:])
        subseq2 = longest_common_subsequence(a[1:], b)
        return subseq1 if len(subseq1) > len(subseq2) else subseq2
