
def bucket_sort(arr, k):
    bucket = [[] for _ in range(k)]
    for x in arr:
        bucket[x].append(x)
    sorted_arr = []
    for bucket in bucket:
        sorted_arr.extend(counting_sort(bucket))
    return sorted_arr

def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    for x in arr:
        count[x] += 1
    sorted_arr = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr
