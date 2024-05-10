
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            if arr[start] == x:
                return start
            else:
                return -1
        else:
            mid = (start + end) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binsearch(start, mid-1)
            else:
                return binsearch(mid+1, end)

    return binsearch(0, len(arr)-1)
