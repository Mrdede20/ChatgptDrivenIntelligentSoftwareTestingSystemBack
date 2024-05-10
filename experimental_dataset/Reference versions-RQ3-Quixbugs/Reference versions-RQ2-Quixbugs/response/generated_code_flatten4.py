Program 1:

```
def flatten(nested_list):
    """
    This function takes a nested list as an argument and returns a generator for its non-list objects.
    
    Input: nested_list (list) - a list with nested lists
    
    Output: generator - a generator object that returns the non-list objects
    
    Example:
    nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
    gen = flatten(nested_list)
    for num in gen:
        print(num)
        
    Output:
    1
    2
    3
    4
    5
    6
    7
    8
    
    """
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
```


Program 2:

```
def flatten(nested_list):
    """
    This function takes a nested list as an argument and returns a generator for its non-list objects.
    
    Input: nested_list (list) - a list with nested lists
    
    Output: generator - a generator object that returns the non-list objects
    
    Example:
    nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
    gen = flatten(nested_list)
    for num in gen:
        print(num)
        
    Output:
    1
    2
    3
    4
    5
    6
    7
    8
    
    """
    for item in nested_list:
        if type(item) == list:
            yield from flatten(item)
        else:
            yield item
```