
def longest_common_subsequence(str1, str2):
    if not str1 or not str2:  # If either of the strings is empty, return empty string
        return ""
    elif str1[0] == str2[0]:  # If the first characters are the same, include it in result and recursively call for the remainder
        return str1[0] + longest_common_subsequence(str1[1:], str2[1:])
    else:  # If the first characters are not same, recursively call both by passing one with the second string's remainder and the other with the first string's remainder
        return max(longest_common_subsequence(str1, str2[1:]), longest_common_subsequence(str1[1:], str2), key=len)
