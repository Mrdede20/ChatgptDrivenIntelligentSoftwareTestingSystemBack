
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = choose_pivot(arr)
    left, right = partition(arr, pivot)
    return quick_sort(left) + [pivot] + quick_sort(right)

def choose_pivot(arr):
    return arr[0]

def partition(arr, pivot):
    left = []
    right = []
    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return left, right
