
def powerset(lst):
    def _powerset(index):
        if index == len(lst):
            return [[]]
        else:
            subsets = _powerset(index + 1)
            return subsets + [[lst[index]] + subset for subset in subsets]

    return _powerset(0)
