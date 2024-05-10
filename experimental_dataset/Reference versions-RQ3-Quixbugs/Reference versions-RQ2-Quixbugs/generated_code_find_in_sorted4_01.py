
def find_in_sorted(arr, value):

    def binsearch(start, end):

        if start > end:
            return -1

        mid = (start + end) // 2

        if arr[mid] == value:
            return mid

        elif arr[mid] > value:
            return binsearch(start, mid-1)

        else:
            return binsearch(mid+1, end)

    return binsearch(0, len(arr)-1)
