Certainly! Here are two functions that achieve this intention:

First program:

```python
def flatten(arr):
    for item in arr:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
```

Second program:

```python
def flatten(arr):
    for item in arr:
        if hasattr(item, '__iter__') and not isinstance(item, str):
            yield from flatten(item)
        else:
            yield item
```

Both of these functions take a list `arr` as input and yield the non-list objects in the flattened list. The first function checks if an element is a list and recursively calls itself if it is, while the second function checks if an element is iterable and not a string before doing the same. In either case, if an element is not a list or iterable, it is immediately yielded.

Both functions use the `yield from` syntax to yield values returned by the recursive call, making them more concise and efficient by reducing the number of temporary lists created in the recursion.