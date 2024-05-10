
def powerset(arr):
    if not arr:
        return [[]]
    else:
        first = arr[0]
        rest_subsets = powerset(arr[1:])
        new_subsets = [subset + [first] for subset in rest_subsets]
        return new_subsets + rest_subsets
