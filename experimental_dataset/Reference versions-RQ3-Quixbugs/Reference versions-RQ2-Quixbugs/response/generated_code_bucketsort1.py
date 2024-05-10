Sure, here are two programs that achieve the same intention:

Program 1:

```python
def bucket_sort(arr, upper_bound):
    counts = [0] * upper_bound
    for num in arr:
        counts[num-1] += 1
    sorted_list = []
    for i in range(upper_bound):
        sorted_list.extend([i+1] * counts[i])
    return sorted_list
```

Program 2:

```python
from collections import defaultdict

def bucket_sort(arr, upper_bound):
    counts = defaultdict(int)
    for num in arr:
        counts[num] += 1
    sorted_list = []
    for i in range(1, upper_bound+1):
        sorted_list.extend([i] * counts[i])
    return sorted_list
```

Both of these programs have the same method name and parameter type, and they both implement the Bucket Sort algorithm in slightly different ways. The first program uses a Python list to count occurrences of each element, while the second program uses a defaultdict from the collections module. The second program also makes the list of counts start from 1 instead of 0.