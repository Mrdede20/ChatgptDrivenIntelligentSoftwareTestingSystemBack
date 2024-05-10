
def binary_search(arr, x):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if arr[mid] == x:
            if mid == start or arr[mid-1] != x:
                return mid
            else:
                end = mid - 1
        
        elif arr[mid] > x:
            end = mid - 1
        
        else:
            start = mid + 1
    
    return -1
