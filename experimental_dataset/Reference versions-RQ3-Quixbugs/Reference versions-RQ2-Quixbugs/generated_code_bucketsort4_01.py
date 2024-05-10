
def bucket_sort(arr, k):
    buckets = [[] for _ in range(k)]
    for val in arr:
        index = val // k
        buckets[index].append(val)
    result = []
    for bucket in buckets:
        if bucket:
            bucket.sort()
            result += bucket
    return result
