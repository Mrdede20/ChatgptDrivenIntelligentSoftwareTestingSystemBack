
def powerset(arr):
    if not arr:
        return [[]]
    else:
        first = arr[0]
        rest = arr[1:]
        rest_power_set = powerset(rest)
        return rest_power_set + [[first] + subset for subset in rest_power_set]
