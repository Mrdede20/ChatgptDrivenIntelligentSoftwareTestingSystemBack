
def bucket_sort(arr, k):
    count = [0] * k
    for x in arr:
        count[x] += 1
    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
