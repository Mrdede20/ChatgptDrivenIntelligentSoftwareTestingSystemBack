
def powerset(lst):
    if not lst:
        return [[]]
    else:
        first = lst[0]
        rest_subsets = powerset(lst[1:])
        return rest_subsets + [[first] + subset for subset in rest_subsets]
