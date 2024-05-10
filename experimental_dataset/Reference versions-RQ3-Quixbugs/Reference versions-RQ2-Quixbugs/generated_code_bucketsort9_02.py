
def bucketsort(arr, k):
    counts = [0] * k
    for i in arr:
        counts[i] += 1
    
    sorted_arr = []
    for i in range(len(counts)):
        for j in range(counts[i]):
            sorted_arr.append(i)
    
    return sorted_arr
