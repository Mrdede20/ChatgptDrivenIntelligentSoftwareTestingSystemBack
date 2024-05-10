Program 1:

```
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
```

Program 2:

```
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
```

Both programs have the same function name `longest_common_subsequence` and take the same parameter type of two strings `a` and `b`. They both use a recursive approach to calculate the longest common subsequence by checking whether either of the strings is empty, or if the first characters of the two strings are the same. If the first characters are different, then the function is called recursively with either the first string and the rest of the second string or the first two characters of the first string and the rest of the second string or vice versa, whichever yields the longest subsequence. If there are multiple subsequences of equal length, either one is returned. 

The difference between the two programs is in how they handle the case of multiple subsequences of equal length. Program 1 uses the built-in `max` function to determine the longest subsequence, while Program 2 uses an `if` statement to compare the length of the two subsequences and return a lexicographically larger subsequence in case of a tie.