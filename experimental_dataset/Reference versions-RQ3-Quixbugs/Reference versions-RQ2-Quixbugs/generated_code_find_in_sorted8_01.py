
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if end >= start:
            mid = start + (end - start) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binsearch(start, mid - 1)
            else:
                return binsearch(mid + 1, end)
        else:
            return -1

    return binsearch(0, len(arr) - 1)
