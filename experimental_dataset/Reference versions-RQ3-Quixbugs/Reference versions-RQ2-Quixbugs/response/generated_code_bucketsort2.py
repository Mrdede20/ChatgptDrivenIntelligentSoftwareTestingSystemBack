Here are two programs that implement the bucket sort algorithm in python:

Program 1:

```
def bucket_sort(arr):
    k = max(arr) + 1
    counts = [0] * k
    for i in arr:
        counts[i] += 1
    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])
    return sorted_arr
```

Program 2:

```
def bucket_sort(arr):
    max_int = max(arr)
    k = max_int + 1
    counts = [0] * k
    for i in arr:
        counts[i] += 1
    sorted_arr = [0] * len(arr)
    j = 0
    for i in range(k):
        for _ in range(counts[i]):
            sorted_arr[j] = i
            j += 1
    return sorted_arr
```

Both programs create an array `counts` to keep track of the number of occurrences of each integer in `arr`. They then create a `sorted_arr` list and populate it the proper number of times with each integer to achieve a sorted list in ascending order. The main difference between the two programs is how they populate `sorted_arr`. 

Program 1 uses the `extend()` method to add each integer the proper number of times to the `sorted_arr` list. Program 2 instead initializes a `sorted_arr` list to the same length as `arr` and uses nested loops to add each integer the proper number of times to the `sorted_arr` list.