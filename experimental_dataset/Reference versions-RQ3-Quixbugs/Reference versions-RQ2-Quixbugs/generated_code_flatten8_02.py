
def flatten(lst):
    for item in lst:
        if type(item) is list:
            yield from flatten(item)
        else:
            yield item
