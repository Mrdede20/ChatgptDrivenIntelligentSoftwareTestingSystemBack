
def bucket_sort(arr, k):
    buckets = {}
    for i in range(k):
        buckets[i] = []
    for val in arr:
        index = val // k
        if index not in buckets:
            buckets[index] = []
        buckets[index].append(val)
    result = []
    for i in range(k):
        if i in buckets:
            buckets[i].sort()
            result += buckets[i]
    return result
