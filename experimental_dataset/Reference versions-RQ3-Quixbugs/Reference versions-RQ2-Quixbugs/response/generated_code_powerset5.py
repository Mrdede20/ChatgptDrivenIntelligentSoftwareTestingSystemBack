Program 1:

```
def powerset(arr):
    if not arr:
        return [[]]
    else:
        first = arr[0]
        rest = arr[1:]
        subsets = powerset(rest)
        return subsets + [[first] + subset for subset in subsets]
```

Program 2:

```
def powerset(arr):
    n = len(arr)
    subsets = []
    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(arr[j])
        subsets.append(subset)
    return subsets
```

Both programs achieve the same intention of generating a list of all possible subsets of the input list 'arr'. The first program uses recursive approach while the second program uses a bitwise approach.