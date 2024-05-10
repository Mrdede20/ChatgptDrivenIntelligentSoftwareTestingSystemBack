
def find_in_sorted(arr, x):
    def binsearch(start, end):
        while end >= start:
            mid = (start + end) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    return binsearch(0, len(arr)-1)
