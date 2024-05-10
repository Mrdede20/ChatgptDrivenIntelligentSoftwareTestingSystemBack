Sure! Here are two examples of Python programs that implement the binary search algorithm with optimizations for time and memory efficiency:

Example 1:

```python
def binary_search_lowest_index(lst, target):
    left, right = 0, len(lst) - 1
    lowest_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            lowest_index = mid
            right = mid - 1
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return lowest_index
```

Example 2:

```python
def binary_search_lowest_index(lst, target):
    left, right = 0, len(lst) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    if lst[left] == target:
        return left
    else:
        return -1
```

Both of these implementations use the same method name and parameter types. In the first example, we keep track of the lowest index that we've found so far, updating it when we find a new target. In the second example, we keep shrinking the search range until we're left with one index, which we check for a target match. Both of these algorithms have time and memory efficiencies built-in for optimal performance on sorted lists.