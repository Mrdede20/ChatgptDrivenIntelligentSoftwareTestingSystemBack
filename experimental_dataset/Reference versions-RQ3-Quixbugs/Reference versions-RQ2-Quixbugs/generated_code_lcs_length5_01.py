
def longest_common_substring(s, t):
    if not s or not t:
        return 0
    counter = [[0] * len(t) for _ in range(len(s))]
    max_length = 0
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                if i == 0 or j == 0:
                    counter[i][j] = 1
                else:
                    counter[i][j] = counter[i-1][j-1] + 1
                max_length = max(max_length, counter[i][j])
    return max_length
