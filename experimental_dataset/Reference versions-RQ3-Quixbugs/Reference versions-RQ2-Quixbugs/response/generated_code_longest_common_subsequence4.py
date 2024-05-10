Program 1:

```
def longest_common_subsequence(a, b):
    if len(a) == 0 or len(b) == 0:
        return ""
    elif a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b[1:])
    else:
        subsequence1 = longest_common_subsequence(a[1:], b)
        subsequence2 = longest_common_subsequence(a, b[1:])
        if len(subsequence1) > len(subsequence2):
            return subsequence1
        else:
            return subsequence2
```

Program 2: (Using memoization)
```
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
```

Both programs achieve the same intention but Program 2 also uses memoization to store previously computed subproblems, making it more efficient for larger inputs.