
def powerset(lst):
    if not lst:
        return [[]]
    else:
        result = []
        for subset in powerset(lst[1:]):
            result.append(subset)
            result.append(subset+[lst[0]])
        return result
