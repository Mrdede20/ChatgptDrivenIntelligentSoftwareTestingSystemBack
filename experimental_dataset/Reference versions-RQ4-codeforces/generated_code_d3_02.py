
def has_non_trivial_valleys(seq):
    n = len(seq)
    valleys = []
    for i in range(1, n-1):
        if seq[i-1] > seq[i] < seq[i+1]:
            valleys.append(i)
    for v in valleys:
        for j in range(v+2, n):
            if seq[j-1] > seq[j]:
                return "YES"
    return "NO"
