
def quicksort(arr):
    def _quicksort(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            _quicksort(arr, low, pivot)
            _quicksort(arr, pivot+1, high)

    def partition(arr, low, high):
        pivot = arr[low]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    _quicksort(arr, 0, len(arr)-1)
    return arr
