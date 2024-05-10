
def powerset(arr):
    if len(arr) == 0:
        return [[]]
    else:
        first = arr[0]
        rest = powerset(arr[1:])
        new = []
        for subset in rest:
            new.append(subset+[first])
        return new + rest
