
def find_lis(seq):
    n = len(seq)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis, default=0)
