
def flatten(lst):
    for elem in lst:
        if isinstance(elem, list):
            yield from flatten(elem)
        else:
            yield elem
