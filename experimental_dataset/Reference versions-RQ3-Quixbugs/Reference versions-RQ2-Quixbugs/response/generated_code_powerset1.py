Here are the two programs:

Program 1: Using Recursion

```python
def powerset(arr):
    if not arr:
        return [[]]
    
    first = arr[0]
    rest = arr[1:]
    rest_subsets = powerset(rest)
    
    new_subsets = [subset + [first] for subset in rest_subsets]
    
    return rest_subsets + new_subsets
```

Program 2: Using Iteration

```python
def powerset(arr):
    subsets = [[]]
    for num in arr:
        subsets += [subset + [num] for subset in subsets]
    return subsets
```

Both programs take a list `arr` as input and recursively or iteratively generate all possible subsets of the list, including the empty set and the entire set. The output of both functions is a list of lists, where each list represents a different subset of `arr`. 

The first program uses recursion to generate the subsets, while the second program uses iteration. The first program extracts the first element of the input list and generates the powerset of the remaining list, then combines this result with the first element to form the powerset of the entire list. The second program iteratively generates subsets by iterating through the input list and adding each element to all existing subsets.