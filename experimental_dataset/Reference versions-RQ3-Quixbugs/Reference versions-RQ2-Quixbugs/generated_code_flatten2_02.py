
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item
