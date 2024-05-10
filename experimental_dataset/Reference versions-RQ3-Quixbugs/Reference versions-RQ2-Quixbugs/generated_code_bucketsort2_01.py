
def bucket_sort(arr):
    k = max(arr) + 1
    counts = [0] * k
    for i in arr:
        counts[i] += 1
    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])
    return sorted_arr
