
def find_LIS(arr):
    n = len(arr)
    ends = {}
    longest = 0

    for i in range(n):
        ends[i] = 1
        for j in range(i):
            if arr[j] < arr[i]:
                ends[i] = max(ends[i], ends[j]+1)
                longest = max(longest, ends[i])

    return longest
