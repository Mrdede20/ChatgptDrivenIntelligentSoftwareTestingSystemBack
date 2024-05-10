
def powerset(arr):
    subsets = [[]]
    for num in arr:
        subsets += [subset + [num] for subset in subsets]
    return subsets
