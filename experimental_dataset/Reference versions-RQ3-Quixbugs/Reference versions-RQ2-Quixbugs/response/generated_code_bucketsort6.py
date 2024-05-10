Sure! Here are two programs that implement Bucket Sort:

Program 1:

```
def bucket_sort(arr, k):
    counts = [0] * k
    for num in arr:
        counts[num] += 1
    sorted_arr = []
    for i in range(k):
        sorted_arr += [i] * counts[i]
    return sorted_arr
```

Program 2:

```
def bucket_sort(arr, k):
    counts = [0 for _ in range(k)]
    for num in arr:
        counts[num] += 1
    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])
    return sorted_arr
```

Both programs achieve the same purpose of implementing Bucket Sort. They take in a list `arr` and an upper bound `k`, and use the `counts` array to count the occurrences of each integer in `arr`. The `sorted_arr` list is then built by iterating over the `counts` array and appending each integer the appropriate number of times to the sorted list.