
def find_in_sorted(arr, value):

    def binsearch(start, end):

        while start <= end:

            mid = (start + end) // 2

            if arr[mid] == value:
                return mid

            elif arr[mid] > value:
                end = mid - 1

            else:
                start = mid + 1

        return -1

    return binsearch(0, len(arr)-1)
