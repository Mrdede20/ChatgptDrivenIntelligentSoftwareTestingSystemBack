
def longest_increasing_subsequence(arr):
    ends = {}
    longest = 0
    for num in arr:
        l, r = 0, longest
        while l < r:
            mid = (l + r) // 2
            if ends[mid] < num:
                l = mid + 1
            else:
                r = mid
        ends[l] = num
        longest = max(longest, l + 1)
    return longest
