
from collections import defaultdict

def bucket_sort(arr, upper_bound):
    counts = defaultdict(int)
    for num in arr:
        counts[num] += 1
    sorted_list = []
    for i in range(1, upper_bound+1):
        sorted_list.extend([i] * counts[i])
    return sorted_list
