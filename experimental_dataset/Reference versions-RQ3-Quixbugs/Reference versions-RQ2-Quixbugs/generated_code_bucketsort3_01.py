
def bucket_sort(arr, k):
    n = len(arr)
    freq = [0] * k
    for i in range(n):
        freq[arr[i]] += 1
    sorted_arr = []
    for i in range(k):
        for j in range(freq[i]):
            sorted_arr.append(i)
    return sorted_arr
