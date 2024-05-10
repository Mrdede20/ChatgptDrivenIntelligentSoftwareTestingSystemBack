
def subsequences(a, b, k):
    if k == 0:
        return [[]]
    if b-a+1 < k:
        return []
    ret = []
    for i in range(a, b+1-k+1):
        current = [[i] + seq for seq in subsequences(i+1, b, k-1)]
        ret.extend(current)
    return ret
