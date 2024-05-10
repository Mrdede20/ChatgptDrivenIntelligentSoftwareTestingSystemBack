
def allSubsequences(a, b, k):
    if k == 0:
        return []
    
    res = []
    for i in range(a, b+1):
        if k == 1:
            res.append([i])
        else:
            subseqs = allSubsequences(i+1, b, k-1)
            for sub in subseqs:
                res.append([i] + sub)
    
    return res
