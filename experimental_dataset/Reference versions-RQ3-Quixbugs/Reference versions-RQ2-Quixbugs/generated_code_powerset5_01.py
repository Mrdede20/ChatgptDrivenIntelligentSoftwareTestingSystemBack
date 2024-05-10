
def powerset(arr):
    if not arr:
        return [[]]
    else:
        first = arr[0]
        rest = arr[1:]
        subsets = powerset(rest)
        return subsets + [[first] + subset for subset in subsets]
