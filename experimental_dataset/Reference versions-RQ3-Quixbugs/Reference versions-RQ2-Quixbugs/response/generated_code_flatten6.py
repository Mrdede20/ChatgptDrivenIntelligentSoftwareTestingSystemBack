Here is the first program that implements the `flatten` method using recursion and a generator function:

```python
def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
```

Here is the second program that implements the same `flatten` method using recursion without a generator function:

```python
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
```

Both programs take a nested list as input and recursively traverse it to yield or return a flattened list of non-list objects. The first program achieves this using a generator function, which yields the output one item at a time, avoiding the need to compute the entire flattened list in memory. The second program achieves the same result using recursion without a generator function, but generates the entire flattened list and returns it all at once, which may not be memory-efficient for very large input lists.