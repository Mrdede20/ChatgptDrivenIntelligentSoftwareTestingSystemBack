Here are two programs which achieves the given intention:

Program 1:
```python
def bucket_sort(arr, k):
    counts = [0] * k
    for num in arr:
        counts[num] += 1
    sorted_arr = []
    for i in range(k):
        for j in range(counts[i]):
            sorted_arr.append(i)
    return sorted_arr
```

Program 2:
```python
def bucket_sort(arr, k):
    n = len(arr)
    counts = [0] * k
    for i in range(n):
        counts[arr[i]] += 1
    index = 0
    for i in range(k):
        for j in range(counts[i]):
            arr[index] = i
            index += 1
    return arr
```

Both these programs implement the Bucket Sort algorithm with the same method name 'bucket_sort' and same parameter type of 'arr' and 'k'. Program 1 uses a separate list 'sorted_arr' to store the sorted elements while program 2 sorts the elements in the original array 'arr' itself.