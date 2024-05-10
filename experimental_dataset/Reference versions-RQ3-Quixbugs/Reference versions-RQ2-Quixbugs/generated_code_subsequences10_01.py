
def subsequences(a, b, k):
    if k == 1:
        return [[i] for i in range(a, b+1)]
    else:
        result = []
        for i in range(a, b-k+2):
            for seq in subsequences(i+1, b, k-1):
                result.append([i] + seq)
        return result
