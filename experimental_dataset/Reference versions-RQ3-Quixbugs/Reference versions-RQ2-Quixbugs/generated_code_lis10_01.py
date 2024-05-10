
def lis(arr):
    ends = {}
    for i in range(len(arr)):
        ends[i] = 1
        for j in range(i):
            if arr[j] < arr[i]:
                ends[i] = max(ends[i], ends[j] + 1)
    return max(ends.values())
