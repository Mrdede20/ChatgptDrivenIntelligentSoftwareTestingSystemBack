
def flatten(lst):
    for elem in lst:
        if isinstance(elem, list):
            for nested_elem in flatten(elem):
                yield nested_elem
        else:
            yield elem
