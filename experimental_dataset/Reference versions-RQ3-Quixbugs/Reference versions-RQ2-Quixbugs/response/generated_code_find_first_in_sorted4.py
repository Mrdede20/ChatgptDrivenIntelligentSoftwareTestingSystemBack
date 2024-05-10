Here are two Python programs that meet the requirements:

Program 1:

```
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            while mid > 0 and arr[mid-1] == target:
                mid -= 1
            return mid
        
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1
```

Program 2:

```
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            index = mid
            while index > 0 and arr[index-1] == target:
                index -= 1
            return index
        
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1
```

Both programs implement a binary search algorithm with a while loop, and update the indexes based on conditions. They check for the first occurrence of the target value in the sorted array by moving backward from the middle index, and return the index where it was found. If the target value is not found, they return -1.