
def bucket_sort(arr, k):
    counts = [0] * k
    for num in arr:
        counts[num] += 1
    sorted_arr = []
    for i in range(k):
        for j in range(counts[i]):
            sorted_arr.append(i)
    return sorted_arr
