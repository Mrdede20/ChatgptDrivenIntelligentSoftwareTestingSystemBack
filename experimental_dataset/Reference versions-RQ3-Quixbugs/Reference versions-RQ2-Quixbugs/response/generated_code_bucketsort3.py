Program 1:

```
def bucket_sort(arr, k):
    n = len(arr)
    freq = [0] * k
    for i in range(n):
        freq[arr[i]] += 1
    sorted_arr = []
    for i in range(k):
        for j in range(freq[i]):
            sorted_arr.append(i)
    return sorted_arr
```

Program 2:

```
def bucket_sort(arr, k):
    n = len(arr)
    freq = [0] * k
    for i in range(n):
        freq[arr[i]] += 1
    sorted_arr = [0] * n
    index = 0
    for i in range(k):
        for j in range(freq[i]):
            sorted_arr[index] = i
            index += 1
    return sorted_arr
```

For both the programs, the input parameters are the same - a list of integers and an upper bound `k`. The first program creates an empty `sorted_arr` list and appends each integer `i`, `(count[i] - 1)` times in ascending order. The second program creates a `sorted_arr` list of the same size as the input list and sets each element to 0. It then iterates through `freq` and sets `sorted_arr` elements based on the frequency of each integer. Both programs implement the bucket sort algorithm and give the same output.