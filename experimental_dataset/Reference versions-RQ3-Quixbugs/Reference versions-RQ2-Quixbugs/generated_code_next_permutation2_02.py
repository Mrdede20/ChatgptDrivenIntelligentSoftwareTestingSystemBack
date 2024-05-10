
def next_permutation(perm):
    n = len(perm)
    i = n - 2

    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1

    if i == -1:
        return sorted(perm)

    j = n - 1
    while perm[j] <= perm[i]:
        j -= 1

    perm[i], perm[j] = perm[j], perm[i]

    left, right = i + 1, n - 1
    while left < right:
        perm[left], perm[right] = perm[right], perm[left]
        left += 1
        right -= 1

    return perm
