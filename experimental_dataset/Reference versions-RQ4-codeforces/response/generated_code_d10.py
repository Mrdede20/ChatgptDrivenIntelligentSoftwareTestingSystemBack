Here are two ways to solve this problem using the `is_subsequence_non_decreasing` method:

### Approach 1: Using bisect_left module

```python
from bisect import bisect_left

def is_subsequence_non_decreasing(arr):
    n = len(arr)
    last_val = [arr[0]]
    for i in range(1, n):
        pos = bisect_left(last_val, arr[i])
        if pos == len(last_val):
            last_val.append(arr[i])
        else:
            last_val[pos] = arr[i]
    return "YES" if len(last_val) > 0 else "NO"
```

### Approach 2: Using simple loop

```python
def is_subsequence_non_decreasing(arr):
    n = len(arr)
    last_val = arr[0]
    for i in range(1, n):
        if arr[i] < last_val:
            last_val = arr[i]
        elif arr[i] >= last_val:
            last_val = arr[i]
    return "YES" if last_val is not None else "NO"
```

Both implementations have the same method name and parameter type: `is_subsequence_non_decreasing(arr)`.