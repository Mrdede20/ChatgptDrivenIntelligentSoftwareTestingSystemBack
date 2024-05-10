Program 1:

```python
def longest_common_subsequence(s1, s2):
    if not s1 or not s2:
        return ""
    elif s1[0] == s2[0]:
        return s1[0] + longest_common_subsequence(s1[1:], s2[1:])
    else:
        lcs1 = longest_common_subsequence(s1[1:], s2)
        lcs2 = longest_common_subsequence(s1, s2[1:])
        return lcs1 if len(lcs1) > len(lcs2) else lcs2
```

Program 2:

```python
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
```

Both programs implement the same `longest_common_subsequence` function that takes two strings as input and returns the longest subsequence common to both strings. Program 1 uses basic recursion to find the LCS whereas Program 2 uses dynamic programming by memoizing the already computed values. Program 2 is more efficient as it avoids redundant calculations by using memoization.