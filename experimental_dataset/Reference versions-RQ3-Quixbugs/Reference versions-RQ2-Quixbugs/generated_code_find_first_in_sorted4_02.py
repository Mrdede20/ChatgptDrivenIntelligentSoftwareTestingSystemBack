
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
