
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        temp = [0]*len(arr)

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                temp[k] = left_half[i]
                i += 1
            else:
                temp[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            temp[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            temp[k] = right_half[j]
            j += 1
            k += 1

        for i in range(len(arr)):
            arr[i] = temp[i]

    return arr
