
def bucket_sort(arr):
    n = len(arr)
    k = max(arr) + 1
    counts = [0] * k
    for i in range(n):
        counts[arr[i]] += 1
    sorted_arr = []
    for i in range(k):
        sorted_arr += [i] * counts[i]
    return sorted_arr
