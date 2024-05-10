1st program:

```
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
```

2nd program:

```
def flatten(nested_list):
    def inner_func(nested_list):
        for item in nested_list:
            if isinstance(item, list):
                yield from inner_func(item)
            else:
                yield item
    return inner_func(nested_list)
```

Both programs define a function called `flatten` that takes a nested list as input and flattens it into a single list using a recursive approach. The `yield` keyword is used to create a generator object that lazily generates the flattened list instead of returning it all at once, making it memory-efficient. 

The first program does this directly in the `flatten` function, while the second program defines a helper function `inner_func` which does the actual flattening and then returns the generator object created by `inner_func`. The `yield from` statement is used to delegate the flattening to the same function recursively.