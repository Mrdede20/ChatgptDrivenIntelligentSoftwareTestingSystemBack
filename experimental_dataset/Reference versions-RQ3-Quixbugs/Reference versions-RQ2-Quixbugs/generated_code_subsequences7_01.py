 
def subsequences(a, b, k):
    if k == 0:
        return []
    ret = []
    for i in range(a, b + 1 - k):
        for seq in subsequences(i+1, b, k-1):
            ret.append([i] + seq)
    return ret
