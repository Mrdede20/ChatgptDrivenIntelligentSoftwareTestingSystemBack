
def powerset(arr):
    subsets = [[]] # initialize with empty set
    for element in arr:
        new_subsets = [subset + [element] for subset in subsets]
        subsets.extend(new_subsets)
    return subsets
