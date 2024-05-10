
def powerset(arr):
    if len(arr) == 0:
        return [[]]
    first = arr[0]
    rest = arr[1:]
    subsets = powerset(rest)
    new_subsets = [subset + [first] for subset in subsets]
    return subsets + new_subsets
