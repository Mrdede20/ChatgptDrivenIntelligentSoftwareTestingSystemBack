
def max_selections(n, c, d, A):

    # Sort the list A in descending order
    A = sorted(A, reverse=True)

    # Check if sum of top d elements in A is greater than or equal to c
    if sum(A[:d]) >= c:
        print("Infinity")
        return

    # Check if maximum value in A multiplied by d is less than c
    if max(A) * d < c:
        print("Impossible")
        return

    # Binary search to find largest possible mid value
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if sum(A[:mid+1]) * (d// (mid+1)) + sum(A[mid+1:]) >= c:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    # Print value of mid-1
    print(result-1)
