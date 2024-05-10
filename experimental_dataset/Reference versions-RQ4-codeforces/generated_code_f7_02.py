
def binary_search(n, arr):
    arr.sort(reverse=True)
    l, r = 0, max(arr)     # set the initial range for binary search
    ans = -1                # initialize the result
    while l <= r:
        mid = (l+r) // 2
        # check if sum of A[i]-mid satisfies the inequality involving c and d
        temp_sum = 0
        for i in range(n):
            if arr[i] > mid:
                temp_sum += arr[i]-mid
        if temp_sum >= mid*c:
            ans = mid   # update the result and continue searching for larger mid
            l = mid+1
        else:
            r = mid-1   # search for smaller mid
    return ans
