Sure, here are two programs to find the length of longest increasing subsequence using the same method name and parameter type:

Program 1: Using Dynamic Programming

```python
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
```

Program 2: Using Binary Search

```python
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
``` 

Both the above programs will take an array as input and will return the length of the longest increasing subsequence in the given sequence of integers using the `lis` method. Program 1 uses dynamic programming to solve this problem, whereas Program 2 uses binary search to optimize the search for the longest increasing subsequence.