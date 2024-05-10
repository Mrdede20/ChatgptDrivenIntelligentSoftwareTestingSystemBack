Sure, here are two possible implementations of the `flatten` function using generator:

### Implementation 1

```python
def flatten(lst):
    for elem in lst:
        if isinstance(elem, list):
            yield from flatten(elem)
        else:
            yield elem
```

In this implementation, we use the `yield from` syntax to delegate to another generator. When we encounter a list element, we recursively call the `flatten` function on that element and yield from it. This way, we flatten the nested lists and return a single flat list.

### Implementation 2

```python
def flatten(lst):
    for elem in lst:
        if isinstance(elem, list):
            for nested_elem in flatten(elem):
                yield nested_elem
        else:
            yield elem
```

In this implementation, we use a basic for loop to iterate over the list elements. When we encounter a list element, we recursively call the `flatten` function on that element and iterate over the flattened sublist using another for loop. This way, we flatten the nested lists and return a single flat list.

Both implementations achieve the same result and use the same method name and parameter type as specified. Let me know if you have any questions!