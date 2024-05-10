
def subsequences(a, b, k):
    if k == 0:
        return [[]]
    else:
        return [sub + [i] for i in range(a, b+1-k) for sub in subsequences(i+1, b, k-1)]
