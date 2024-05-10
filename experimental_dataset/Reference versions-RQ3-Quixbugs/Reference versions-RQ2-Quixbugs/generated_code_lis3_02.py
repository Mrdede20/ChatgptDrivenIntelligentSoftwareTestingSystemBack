
def longest_increasing_subsequence(seq, ends={}):
    n = len(seq)
    if n not in ends:
        ends[n] = 1
        for i in range(n-1, -1, -1):
            if seq[i] < seq[n-1]:
                ends[n] = max(ends[n], longest_increasing_subsequence(seq[:i+1], ends)+1)
    return ends[n]
