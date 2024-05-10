Here are two programs that implement the Bucket Sort algorithm using different methods:


Method 1:
```
def bucket_sort(arr, k):
    bucket = [[] for _ in range(k)]
    for x in arr:
        bucket[x].append(x)
    sorted_arr = []
    for bucket in bucket:
        sorted_arr.extend(counting_sort(bucket))
    return sorted_arr

def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    for x in arr:
        count[x] += 1
    sorted_arr = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr
```

Method 2:
```
def bucket_sort(arr, k):
    count = [0] * k
    for x in arr:
        count[x] += 1
    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
```

Both methods implement the bucket sort algorithm by first filling buckets with the input data and then sorting them using the counting sort algorithm. Method 1 uses a second function to sort the buckets, while Method 2 performs the counting sort algorithm directly in the `bucket_sort()` function.