
def lis(arr):
    ends = {}
    longest = 0
    for num in arr:
        if not ends:
            ends[1] = num
            longest = 1
        else:
            left, right = 1, longest
            while left <= right:
                mid = (left + right) // 2
                if ends[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            ends[left] = num
            longest = max(longest, left)
    return longest
