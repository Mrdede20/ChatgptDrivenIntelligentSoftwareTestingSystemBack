
def generate_subsequences(a, b, k):
    if k == 0:
        return []
    if k == 1:
        return [[i] for i in range(a, b+1)]
    ret = []
    for i in range(a, b+1):
        subsequences = generate_subsequences(i+1, b, k-1)
        for subsequence in subsequences:
            ret.append([i]+subsequence)
    return ret
