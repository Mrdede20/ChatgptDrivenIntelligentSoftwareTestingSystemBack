
def binary_search(arr, x, start, end):
    if end >= start:
        mid = start + (end - start) // 2
        
        if arr[mid] == x:
            if mid == start or arr[mid-1] != x:
                return mid
            else:
                return binary_search(arr, x, start, mid-1)
        
        elif arr[mid] > x:
            return binary_search(arr, x, start, mid-1)
        
        else:
            return binary_search(arr, x, mid+1, end)
    
    else:
        return -1
