
def modified_binary_search(arr, x):
    def recurse(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid-1] != x:
                return mid
            else:
                return recurse(low, mid-1)
        elif arr[mid] < x:
            return recurse(mid+1, high)
        else:
            return recurse(low, mid-1)
    return recurse(0, len(arr)-1)
