
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    else:
        pivot = arr[0]
        lower = [i for i in arr[1:] if i <= pivot]
        upper = [i for i in arr[1:] if i > pivot]

        if k < len(lower):
            return quickselect(lower, k)
        elif k == len(lower):
            return pivot
        else:
            new_k = k - len(lower) - 1
            return quickselect(upper, new_k)
