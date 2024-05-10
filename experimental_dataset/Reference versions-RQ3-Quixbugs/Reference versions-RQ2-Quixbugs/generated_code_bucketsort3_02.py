
def bucket_sort(arr, k):
    n = len(arr)
    freq = [0] * k
    for i in range(n):
        freq[arr[i]] += 1
    sorted_arr = [0] * n
    index = 0
    for i in range(k):
        for j in range(freq[i]):
            sorted_arr[index] = i
            index += 1
    return sorted_arr
