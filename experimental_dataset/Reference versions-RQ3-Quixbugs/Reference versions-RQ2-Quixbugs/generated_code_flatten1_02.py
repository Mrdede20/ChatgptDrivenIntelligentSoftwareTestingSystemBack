
def flatten(nested_list):
    for item in nested_list:
        if type(item) == list:
            yield from flatten(item)
        else:
            yield item
