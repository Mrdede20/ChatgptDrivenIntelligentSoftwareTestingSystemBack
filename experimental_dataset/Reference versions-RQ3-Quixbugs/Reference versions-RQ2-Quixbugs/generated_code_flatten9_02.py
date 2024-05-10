
def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            for sub_item in flatten(item):
                yield sub_item
        else:
            yield item
