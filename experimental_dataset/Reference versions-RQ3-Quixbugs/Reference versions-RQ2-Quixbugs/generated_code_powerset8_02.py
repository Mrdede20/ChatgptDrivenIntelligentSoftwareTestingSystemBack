
def powerset(arr):
    def _powerset(i):
        if i == len(arr):
            return [[]]
        subsets = _powerset(i + 1)
        new_subsets = [subset + [arr[i]] for subset in subsets if subset + [arr[i]] not in subsets]
        return subsets + new_subsets
    return _powerset(0)
