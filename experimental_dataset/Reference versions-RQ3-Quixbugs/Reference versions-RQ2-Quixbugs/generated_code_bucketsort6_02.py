
def bucket_sort(arr, k):
    counts = [0 for _ in range(k)]
    for num in arr:
        counts[num] += 1
    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])
    return sorted_arr
