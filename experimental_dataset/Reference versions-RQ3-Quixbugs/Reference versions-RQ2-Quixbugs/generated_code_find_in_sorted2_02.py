
def binsearch(arr, x, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
            
    return -1
