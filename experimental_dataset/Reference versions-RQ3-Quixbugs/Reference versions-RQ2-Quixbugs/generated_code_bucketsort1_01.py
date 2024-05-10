
def bucket_sort(arr, upper_bound):
    counts = [0] * upper_bound
    for num in arr:
        counts[num-1] += 1
    sorted_list = []
    for i in range(upper_bound):
        sorted_list.extend([i+1] * counts[i])
    return sorted_list
