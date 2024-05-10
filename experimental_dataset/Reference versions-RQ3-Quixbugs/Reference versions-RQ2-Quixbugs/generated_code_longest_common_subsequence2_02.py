
def longest_common_subsequence(str1, str2):
    if not str1 or not str2:  # If either of the strings is empty, return empty string
        return ""
    elif str1[-1] == str2[-1]:  # If the last characters are the same, include it in result and recursively call for the remainder in reverse
        return longest_common_subsequence(str1[:-1], str2[:-1]) + str1[-1]
    else:  # If the last characters are not same, recursively call both by passing the one with the maximum length
        seq1 = longest_common_subsequence(str1, str2[:-1])
        seq2 = longest_common_subsequence(str1[:-1], str2)
        return seq1 if len(seq1) > len(seq2) else seq2
