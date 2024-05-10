
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binsearch(mid+1, end)
        else:
            return binsearch(start, mid-1)
    return binsearch(0, len(arr)-1)
