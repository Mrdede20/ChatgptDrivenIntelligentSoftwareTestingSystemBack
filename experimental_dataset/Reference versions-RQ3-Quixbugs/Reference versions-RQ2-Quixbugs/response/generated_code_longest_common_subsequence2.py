Here are two programs implementing the same method using recursion:

Program 1:

```
def longest_common_subsequence(str1, str2):
    if not str1 or not str2:  # If either of the strings is empty, return empty string
        return ""
    elif str1[0] == str2[0]:  # If the first characters are the same, include it in result and recursively call for the remainder
        return str1[0] + longest_common_subsequence(str1[1:], str2[1:])
    else:  # If the first characters are not same, recursively call both by passing one with the second string's remainder and the other with the first string's remainder
        return max(longest_common_subsequence(str1, str2[1:]), longest_common_subsequence(str1[1:], str2), key=len)
```

Program 2: 

```
def longest_common_subsequence(str1, str2):
    if not str1 or not str2:  # If either of the strings is empty, return empty string
        return ""
    elif str1[-1] == str2[-1]:  # If the last characters are the same, include it in result and recursively call for the remainder in reverse
        return longest_common_subsequence(str1[:-1], str2[:-1]) + str1[-1]
    else:  # If the last characters are not same, recursively call both by passing the one with the maximum length
        seq1 = longest_common_subsequence(str1, str2[:-1])
        seq2 = longest_common_subsequence(str1[:-1], str2)
        return seq1 if len(seq1) > len(seq2) else seq2
```

Both programs take two strings as input parameters and implement the approach of breaking down the problem into sub-problems and solving them recursively. However, they differ in how they compare the subproblems to determine the longest common subsequence. Program 1 checks for the first characters while program 2 checks for the last characters.