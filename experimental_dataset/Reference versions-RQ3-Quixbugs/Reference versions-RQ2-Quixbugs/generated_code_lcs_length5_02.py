
def longest_common_substring(s, t):
    if not s or not t:
        return 0
    counter = [[0] * (len(t)+1) for _ in range(len(s)+1)]
    max_length = 0
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                counter[i][j] = counter[i-1][j-1] + 1
                max_length = max(max_length, counter[i][j])
    return max_length
