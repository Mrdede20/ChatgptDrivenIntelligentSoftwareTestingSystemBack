
def longest_increasing_subsequence(sequence):
    dp = [1] * len(sequence)

    for i in range(len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)
