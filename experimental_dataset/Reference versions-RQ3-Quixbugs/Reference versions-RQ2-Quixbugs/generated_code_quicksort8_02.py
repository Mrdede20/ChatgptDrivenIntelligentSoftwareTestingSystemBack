
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        left = []
        right = []
        for item in arr:
            if item < pivot:
                left.append(item)
            else:
                right.append(item)
        return quick_sort(left) + [pivot] + quick_sort(right)
