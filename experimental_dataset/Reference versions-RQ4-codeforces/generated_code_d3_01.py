
def has_non_trivial_valleys(seq):
    n = len(seq)
    for i in range(1, n-1):
        if seq[i-1] > seq[i] < seq[i+1]:
            for j in range(i+2, n):
                if seq[j-1] > seq[j]:
                    return "YES"
            return "NO"
    return "NO"
