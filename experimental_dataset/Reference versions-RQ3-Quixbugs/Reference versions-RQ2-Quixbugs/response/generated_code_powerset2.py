Sure, here's the first implementation:

```python
def powerset(lst):
    if not lst:
        return [[]]
    else:
        first = lst[0]
        rest_subsets = powerset(lst[1:])
        return rest_subsets + [[first] + subset for subset in rest_subsets]
```

And here's the second implementation which uses a helper function to avoid creating a new list for every subset:

```python
def powerset(lst):
    def _powerset(index):
        if index == len(lst):
            return [[]]
        else:
            subsets = _powerset(index + 1)
            return subsets + [[lst[index]] + subset for subset in subsets]

    return _powerset(0)
```

Both implementations work recursively and return the same output for any given input list.