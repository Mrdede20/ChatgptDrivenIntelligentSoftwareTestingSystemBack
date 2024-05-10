
def lis(arr):
    n = len(arr)
    # Initialize the ends dictionary with the first element
    ends = {0: arr[0]}
 
    # Initialize the longest variable
    longest = 1
 
    # Find the length of the longest increasing subsequence
    for i in range(1, n):
        if arr[i] > ends[longest-1]:
            ends[longest] = arr[i]
            longest += 1
        else:
            j = longest - 1
            while j >= 0 and arr[i] < ends[j]:
                j -= 1
            ends[j+1] = arr[i]
            
    return longest
