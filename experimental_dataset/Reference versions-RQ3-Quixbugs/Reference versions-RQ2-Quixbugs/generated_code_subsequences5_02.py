
def subsequences(a, b, k):
    if k == 0:
        return [[]]
    if b - a + 1 < k:
        return []
    result = []
    for i in range(a, b+1-k+1):
        for seq in subsequences(i+1, b, k-1):
            result.append([i] + seq)
    return result
