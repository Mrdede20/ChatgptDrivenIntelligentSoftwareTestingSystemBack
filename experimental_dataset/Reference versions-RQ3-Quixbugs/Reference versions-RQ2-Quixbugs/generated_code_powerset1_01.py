
def powerset(arr):
    if not arr:
        return [[]]
    
    first = arr[0]
    rest = arr[1:]
    rest_subsets = powerset(rest)
    
    new_subsets = [subset + [first] for subset in rest_subsets]
    
    return rest_subsets + new_subsets
