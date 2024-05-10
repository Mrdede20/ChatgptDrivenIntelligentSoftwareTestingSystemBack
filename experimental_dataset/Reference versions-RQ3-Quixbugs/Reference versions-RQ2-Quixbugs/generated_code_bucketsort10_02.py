
def bucket_sort(arr, k):
    n = len(arr)
    counts = [0] * k
    for i in range(n):
        counts[arr[i]] += 1
    index = 0
    for i in range(k):
        for j in range(counts[i]):
            arr[index] = i
            index += 1
    return arr
