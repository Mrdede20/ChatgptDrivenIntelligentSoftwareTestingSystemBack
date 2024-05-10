
def find_in_sorted(arr, x):
    def binsearch(start, end):
        mid = start + (end - start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            if start == end:
                return -1
            return binsearch(start, mid)
        else:
            if start == end:
                return -1
            return binsearch(mid + 1, end)

    return binsearch(0, len(arr) - 1)
