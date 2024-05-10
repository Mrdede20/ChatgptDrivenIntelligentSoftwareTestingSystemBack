Here is the first implementation of the LIS algorithm:

```python
def find_LIS(arr):
    n = len(arr)
    ends = {}
    longest = 0

    for i in range(n):
        ends[i] = 1
        for j in range(i):
            if arr[j] < arr[i]:
                ends[i] = max(ends[i], ends[j]+1)
                longest = max(longest, ends[i])

    return longest
```
The time complexity of this implementation is O(n^2).

Here is a second implementation of the LIS algorithm using the binary search:

```python
from bisect import bisect_left

def find_LIS(arr):
    n = len(arr)
    ends = []

    for i in range(n):
        idx = bisect_left(ends, arr[i])
        if idx == len(ends):
            ends.append(arr[i])
        else:
            ends[idx] = arr[i]

    return len(ends)
```
The time complexity of this implementation is O(n*log(n)).