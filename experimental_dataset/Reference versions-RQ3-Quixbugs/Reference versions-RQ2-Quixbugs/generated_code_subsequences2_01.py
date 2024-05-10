
def allSubsequences(a, b, k):
    if k == 0:
        return []
    
    if k == 1:
        return [[i] for i in range(a, b+1)]
    
    res = []
    for i in range(a, b+1):
        subseqs = allSubsequences(i+1, b, k-1)
        for sub in subseqs:
            res.append([i] + sub)
    
    return res
