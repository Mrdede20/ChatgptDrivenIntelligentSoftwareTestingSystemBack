Here are two versions of the `powerset` function in Python:

Version 1: Using Recursion

```python
def powerset(arr):
    if not arr:
        return [[]] # base case: empty set is a subset of every set
    else:
        rest = powerset(arr[1:]) # get all subsets of remaining elements
        return rest + [[arr[0]] + subset for subset in rest] 
        # combine with subsets that include first element
```
Version 2: Using Iteration

```python
def powerset(arr):
    subsets = [[]] # initialize with empty set
    for element in arr:
        new_subsets = [subset + [element] for subset in subsets]
        subsets.extend(new_subsets)
    return subsets
```

Both versions of the function take a list `arr` as input and return a list of all the possible subsets of `arr`, including the empty set and `arr` itself. The first version uses recursion to generate the subsets, while the second version uses iteration. The output of both functions is the same.

Note that both functions assume that `arr` has no duplicate elements, so they may not work correctly for lists with duplicates. Also note that the second version of the function uses list comprehension and `extend` method instead of using `append` method.