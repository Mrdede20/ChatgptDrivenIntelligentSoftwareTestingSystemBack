
def flatten(arr):
    for item in arr:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
