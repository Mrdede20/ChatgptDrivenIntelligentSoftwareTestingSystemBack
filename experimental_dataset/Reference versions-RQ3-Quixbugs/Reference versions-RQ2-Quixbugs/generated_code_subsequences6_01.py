
def generate_subsequences(a, b, k):
    if k == 0:
        return [[]]
    elif a > b:
        return []
    else:
        result = []
        for i in range(a, b+1):
            subsequences = generate_subsequences(i+1, b, k-1)
            for subseq in subsequences:
                result.append([i] + subseq)
        return result
