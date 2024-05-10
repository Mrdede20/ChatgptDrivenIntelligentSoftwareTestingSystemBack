
def max_subarray_sum(arr):
    n = len(arr)
    max_sum = arr[0]
    temp_sum = arr[0]
    for i in range(1, n):
        temp_sum = max(arr[i], temp_sum+arr[i])
        max_sum = max(temp_sum, max_sum)
    return max_sum
