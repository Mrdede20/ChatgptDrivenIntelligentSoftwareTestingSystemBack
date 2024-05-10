
def bucket_sort(arr):
    n = len(arr)
    max_num = max(arr)
    count = [0] * (max_num + 1)
    for i in range(n):
        count[arr[i]] += 1
    sorted_arr = []
    for i in range(max_num + 1):
        for j in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr
