Program 1: 

```python
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)

arr = [8, 4, 2, 10, 3, 6]
print(quicksort(arr))
```

Output:
```
[2, 3, 4, 6, 8, 10]
```

Program 2: 

```python
def quicksort(arr):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
        
    def helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            helper(arr, low, pi-1)
            helper(arr, pi+1, high)
    
    helper(arr, 0, len(arr)-1)
    return arr
    
arr = [8, 4, 2, 10, 3, 6]
print(quicksort(arr))
```

Output:

```
[2, 3, 4, 6, 8, 10]
```