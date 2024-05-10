
def longest_increasing_subsequence(sequence):
    ends = {}
    longest = 0

    for num in sequence:
        i, j = 0, longest
        while i != j:
            mid = (i + j) // 2
            if ends[mid] < num:
                i = mid + 1
            else:
                j = mid
        ends[i] = num
        longest = max(longest, i+1)

    return longest
