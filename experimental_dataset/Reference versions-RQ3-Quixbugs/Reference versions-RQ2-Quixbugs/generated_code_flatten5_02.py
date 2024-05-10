
def flatten(nested_list):
    def inner_func(nested_list):
        for item in nested_list:
            if isinstance(item, list):
                yield from inner_func(item)
            else:
                yield item
    return inner_func(nested_list)
