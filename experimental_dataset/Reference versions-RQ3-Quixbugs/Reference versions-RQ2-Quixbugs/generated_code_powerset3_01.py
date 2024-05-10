
def powerset(lst):
    result = [[]]
    for x in lst:
        newset = [subset+[x] for subset in result]
        result.extend(newset)
    return result
