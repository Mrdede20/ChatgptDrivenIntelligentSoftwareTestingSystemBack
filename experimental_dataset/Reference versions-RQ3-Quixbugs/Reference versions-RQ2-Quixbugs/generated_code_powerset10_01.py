
def powerset(arr):
    if not arr:
        return [[]] # base case: empty set is a subset of every set
    else:
        rest = powerset(arr[1:]) # get all subsets of remaining elements
        return rest + [[arr[0]] + subset for subset in rest] 
        # combine with subsets that include first element
