Program 1:

```
def powerset(arr):
    if not arr:
        return [[]]
    else:
        first = arr[0]
        rest = arr[1:]
        rest_power_set = powerset(rest)
        return rest_power_set + [[first] + subset for subset in rest_power_set]
```

Program 2:

```
def powerset(arr):
    def generate(idx, current):
        if idx == len(arr):
            return [current]
        else:
            return generate(idx+1, current) + generate(idx+1, current+[arr[idx]])
        
    return generate(0, [])
```

Both of these programs acheive the same result of generating the power set of a given list. Program 1 uses recursion to split the list into a first element and the rest of the list, and then uses the rest list power set to construct the power set of the entire list. Program 2 uses a nested function called generate to generate all possible subsets of the list by recursively choosing each element either to be in the current subset or not.