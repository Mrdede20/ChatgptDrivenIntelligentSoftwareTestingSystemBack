
def bucket_sort(arr):
    max_int = max(arr)
    k = max_int + 1
    counts = [0] * k
    for i in arr:
        counts[i] += 1
    sorted_arr = [0] * len(arr)
    j = 0
    for i in range(k):
        for _ in range(counts[i]):
            sorted_arr[j] = i
            j += 1
    return sorted_arr
