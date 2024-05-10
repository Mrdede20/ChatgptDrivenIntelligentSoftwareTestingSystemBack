Sure, here are two possible implementations of the `flatten` function:

Implementation 1:

```python
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
```

Implementation 2:

```python
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item
```

Both implementations use recursion to handle arbitrary levels of nesting in the input list. The `isinstance` function is used to determine if an element is a list or not. If it's not a list, it's immediately yielded. If it is a list, either `yield from` or a nested loop is used to recursively call the `flatten` function on the sublist.

Both implementations return a generator, which allows the function to generate the flattened output in a memory-efficient manner instead of creating a new list.