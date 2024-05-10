
def longest_increasing_subsequence(seq):
    n = len(seq)
    ends = {}
    longest = 0
    for i in range(n):
        ends[i] = 1
        for j in range(i):
            if seq[j] < seq[i]:
                ends[i] = max(ends[i], ends[j]+1)
        longest = max(longest, ends[i])
    return longest
