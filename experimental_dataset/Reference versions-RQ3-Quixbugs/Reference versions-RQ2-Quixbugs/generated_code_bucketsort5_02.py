
def bucket_sort(arr, k):
    counts = [0] * k
    for num in arr:
        counts[num] += 1
    
    sorted_arr = [num for num, count in enumerate(counts) for _ in range(count)]
    
    return sorted_arr
