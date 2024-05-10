
def flatten(arr):
    for item in arr:
        if hasattr(item, '__iter__') and not isinstance(item, str):
            yield from flatten(item)
        else:
            yield item
