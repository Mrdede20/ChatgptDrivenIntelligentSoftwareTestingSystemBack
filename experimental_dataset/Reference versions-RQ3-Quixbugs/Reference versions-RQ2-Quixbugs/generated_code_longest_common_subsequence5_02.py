
def longest_common_subsequence(str1, str2):
    memo = {}
    def subsequence_helper(str1, str2):
        if (str1, str2) in memo:
            return memo[(str1, str2)]
        if len(str1) == 0 or len(str2) == 0:
            result = ""
        elif str1[0] == str2[0]:
            result = str1[0] + subsequence_helper(str1[1:], str2[1:])
        else:
            result = max(subsequence_helper(str1[1:], str2), subsequence_helper(str1, str2[1:]), key=len)
        memo[(str1, str2)] = result
        return result
    return subsequence_helper(str1, str2)
