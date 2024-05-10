
def next_permutation(lst):
    i = len(lst) - 2
    while i >= 0 and lst[i] >= lst[i + 1]:
        i -= 1
    if i == -1:
        return lst[::-1]
    j = len(lst) - 1
    while lst[j] <= lst[i]:
        j -= 1
    lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1:] = lst[:i:-1]
    return lst
