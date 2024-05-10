
def longest_increasing_subsequence(arr):
    ends = []
    for num in arr:
        l, r = 0, len(ends)
        while l < r:
            mid = (l + r) // 2
            if ends[mid] < num:
                l = mid + 1
            else:
                r = mid
        if l == len(ends):
            ends.append(num)
        else:
            ends[l] = num
    return len(ends)
