
def subsequences(a, b, k):
    if k == 0:
        return [[]]
    else:
        subs = []
        for i in range(a, b+1-k):
            for sub in subsequences(i+1, b, k-1):
                subs.append([i] + sub)
        return subs
