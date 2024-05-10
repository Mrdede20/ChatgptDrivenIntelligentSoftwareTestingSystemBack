
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
