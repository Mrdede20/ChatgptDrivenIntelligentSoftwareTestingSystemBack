
def longest_common_subsequence(a, b, cache={}):
    if (a, b) in cache:
        return cache[(a, b)]
    elif len(a) == 0 or len(b) == 0:
        return ""
    elif a[0] == b[0]:
        result = a[0] + longest_common_subsequence(a[1:], b[1:], cache)
    else:
        subsequence1 = longest_common_subsequence(a[1:], b, cache)
        subsequence2 = longest_common_subsequence(a, b[1:], cache)
        if len(subsequence1) > len(subsequence2):
            result = subsequence1
        else:
            result = subsequence2
    cache[(a, b)] = result
    return result
