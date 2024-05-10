Here is the first program that implements the "Longest Common Subsequence" algorithm using recursion without dynamic programming:

```
def longest_common_subsequence(str1, str2):
    if not str1 or not str2:
        return ""
    elif str1[0] == str2[0]:
        return str1[0] + longest_common_subsequence(str1[1:], str2[1:])
    else:
        result1 = longest_common_subsequence(str1[1:], str2)
        result2 = longest_common_subsequence(str1, str2[1:])
        return result1 if len(result1) > len(result2) else result2
```

Here is the second program that implements the "Longest Common Subsequence" algorithm using dynamic programming:

```
def longest_common_subsequence(str1, str2):
    matrix = [[0 for x in range(len(str2)+1)] for y in range(len(str1)+1)]
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    result = ""
    i, j = len(str1), len(str2)
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            result = str1[i-1] + result
            i -= 1
            j -= 1
        elif matrix[i-1][j] > matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    return result
```
Both programs have the same method name `longest_common_subsequence` and the same parameter type, which is two strings.