
def longest_common_subsequence(str1, str2):
    if not str1 or not str2:
        return ""
    elif str1[0] == str2[0]:
        return str1[0] + longest_common_subsequence(str1[1:], str2[1:])
    else:
        result1 = longest_common_subsequence(str1[1:], str2)
        result2 = longest_common_subsequence(str1, str2[1:])
        return result1 if len(result1) > len(result2) else result2
