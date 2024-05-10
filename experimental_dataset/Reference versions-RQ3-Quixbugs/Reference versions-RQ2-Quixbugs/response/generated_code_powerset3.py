Program 1: Iterative Solution

```python
def powerset(lst):
    result = [[]]
    for x in lst:
        newset = [subset+[x] for subset in result]
        result.extend(newset)
    return result
```

Program 2: Recursive Solution

```python
def powerset(lst):
    if not lst:
        return [[]]
    else:
        result = []
        for subset in powerset(lst[1:]):
            result.append(subset)
            result.append(subset+[lst[0]])
        return result
```