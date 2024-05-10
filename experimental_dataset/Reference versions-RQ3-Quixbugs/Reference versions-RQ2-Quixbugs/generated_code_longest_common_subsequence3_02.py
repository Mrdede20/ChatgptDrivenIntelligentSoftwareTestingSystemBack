
def longest_common_subsequence(a, b):
    if len(a) == 0 or len(b) == 0:
        return ""
    elif a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b[1:])
    else:
        sub1 = longest_common_subsequence(a[1:], b)
        sub2 = longest_common_subsequence(a, b[1:])
        if len(sub1) > len(sub2):
            return sub1
        elif len(sub2) > len(sub1):
            return sub2
        else:
            return sub1 if sub1 > sub2 else sub2
