 
def subsequences(a, b, k):
    if k == 0:
        return []
    if k == 1:
        return [[i] for i in range(a, b+1)]
    return [[i]+seq for i in range(a, b+1-k+1) for seq in subsequences(i+1, b, k-1)]
