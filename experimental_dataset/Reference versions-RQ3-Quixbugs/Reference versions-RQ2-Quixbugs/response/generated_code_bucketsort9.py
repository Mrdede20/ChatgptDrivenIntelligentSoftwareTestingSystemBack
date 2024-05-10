Here are two implementations of the `bucketsort` function in Python:

**First implementation:**

```python
def bucketsort(arr, k):
    counts = [0] * k
    for num in arr:
        counts[num] += 1
    
    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])
    
    return sorted_arr
```

**Second implementation:**

```python
def bucketsort(arr, k):
    counts = [0] * k
    for i in arr:
        counts[i] += 1
    
    sorted_arr = []
    for i in range(len(counts)):
        for j in range(counts[i]):
            sorted_arr.append(i)
    
    return sorted_arr
```

Both implementations should give the same result for a given input. The first implementation uses `extend` to concatenate the list of i's to the `sorted_arr` list, while the second implementation uses a nested loop to append each i j times to `sorted_arr`.