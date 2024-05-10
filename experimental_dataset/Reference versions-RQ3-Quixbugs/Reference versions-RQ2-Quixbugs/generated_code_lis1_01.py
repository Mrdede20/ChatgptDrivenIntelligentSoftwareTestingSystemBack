
def lis(arr):
    n = len(arr)
    # Initialize the ends dictionary
    ends = {}
    for i in range(n):
        ends[i] = 1
 
    # Initialize the longest variable
    longest = 1
 
    # Find the length of the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                ends[i] = max(ends[i], ends[j]+1)
                longest = max(longest, ends[i])
                
    return longest
