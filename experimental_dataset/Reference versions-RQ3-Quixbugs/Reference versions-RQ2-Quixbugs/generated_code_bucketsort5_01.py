
def bucket_sort(arr, k):
    counts = [0] * k
    for num in arr:
        counts[num] += 1
    
    sorted_arr = []
    for i, count in enumerate(counts):
        sorted_arr += [i] * count
    
    return sorted_arr
