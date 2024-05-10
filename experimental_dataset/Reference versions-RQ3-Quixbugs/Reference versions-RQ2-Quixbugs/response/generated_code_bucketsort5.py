Here are two examples of programs implementing the Bucket Sort algorithm:

Program 1:
```python
def bucket_sort(arr, k):
    counts = [0] * k
    for num in arr:
        counts[num] += 1
    
    sorted_arr = []
    for i, count in enumerate(counts):
        sorted_arr += [i] * count
    
    return sorted_arr
```

Program 2:
```python
def bucket_sort(arr, k):
    counts = [0] * k
    for num in arr:
        counts[num] += 1
    
    sorted_arr = [num for num, count in enumerate(counts) for _ in range(count)]
    
    return sorted_arr
``` 

Both programs have the same method name `bucket_sort` and take in the same parameters `arr` and `k`. The first program creates an empty `sorted_arr` list and iterates over every integer `i` in `counts`, adding `count` copies of `i` to `sorted_arr`. The second program uses a list comprehension to create the `sorted_arr` list. The resulting `sorted_arr` list contains all the elements of `arr`, sorted in non-decreasing order, as per the Bucket Sort algorithm.