Here are two programs which achieve this intention:

Program 1:
```python
def powerset(arr):
    if not arr:
        return [[]]
    else:
        first = arr[0]
        rest_subsets = powerset(arr[1:])
        new_subsets = [subset + [first] for subset in rest_subsets]
        return new_subsets + rest_subsets
```

Program 2:
```python
def powerset(arr):
    if len(arr) == 0:
        return [[]]
    else:
        first = arr[0]
        rest = powerset(arr[1:])
        new = []
        for subset in rest:
            new.append(subset+[first])
        return new + rest
```

Both programs follow the same logic and produce the same output. Both programs have the same function name (`powerset`) and parameter type (`arr`), as specified in the prompt.