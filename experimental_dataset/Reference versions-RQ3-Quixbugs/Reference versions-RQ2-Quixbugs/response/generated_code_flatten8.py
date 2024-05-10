Here are two programs that achieve the same goal:

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
        if type(item) is list:
            yield from flatten(item)
        else:
            yield item
```

Both programs use a generator function called "flatten" that accepts a nested list as input and returns a generator that yields its non-list objects in a flattened way. 

The function uses recursion to iterate over the given list and its sub-lists. Whenever a non-list item is encountered, it is yielded to the caller. If a sub-list is encountered, the function is called recursively with the sub-list as argument. 

Both programs have the same method name and parameter type, and achieve the same desired outcome efficiently and in a memory-friendly way.