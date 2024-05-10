Here are two programs that achieve the intention:

Program 1:
```
def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
```

Program 2:
```
def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            for sub_item in flatten(item):
                yield sub_item
        else:
            yield item
```

Both of these programs use the same method name and parameter type. The only difference is how the recursive call to `flatten` is made. In Program 1, the `yield from` statement is used to directly yield the results of the recursive call without using an additional loop. In Program 2, a nested loop is used to yield each individual element from the recursive call separately.

Both programs achieve the intention of recursively flattening a nested list structure into a single list using a generator, while also being memory efficient.