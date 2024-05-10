
def powerset(arr):
    if not arr:
        return [[]]
    else:
        result = []
        for subset in powerset(arr[1:]):
            result.append(subset)
            result.append([arr[0]] + subset)
        return result
