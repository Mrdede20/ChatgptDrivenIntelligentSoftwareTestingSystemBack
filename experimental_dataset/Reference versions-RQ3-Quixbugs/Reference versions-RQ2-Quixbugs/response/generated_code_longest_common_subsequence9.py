Program 1:

```
def longest_common_subsequence(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return ""
    elif str1[0] == str2[0]:
        return str1[0] + longest_common_subsequence(str1[1:], str2[1:])
    else:
        lcs1 = longest_common_subsequence(str1[1:], str2)
        lcs2 = longest_common_subsequence(str1, str2[1:])
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2
```

Program 2:

```
def longest_common_subsequence(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return ""
    elif str1[0] == str2[0]:
        return str1[0] + longest_common_subsequence(str1[1:], str2[1:])
    else:
        lcs1 = longest_common_subsequence(str1[1:], str2)
        lcs2 = longest_common_subsequence(str1, str2[1:])
        return max(lcs1, lcs2, key=len)
```

Both programs implement the same recursive approach to calculate the longest common subsequence of two input strings. The first program uses an if-else statement to compare the two subsequences obtained by removing the first character from the first string and from the second string. Then, it returns the longest subsequence by comparing the lengths of these two subsequences. 

The second program simplifies the if-else statement by using the built-in `max` function with the optional `key` parameter, which specifies the function to be used to determine the maximum value in the iterable. In this case, we use the `len` function as the key to compare the lengths of `lcs1` and `lcs2`.