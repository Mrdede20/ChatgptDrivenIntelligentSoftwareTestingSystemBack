# Take the number of test cases as input
t = int(input())

# Iterate through each test case
for i in range(t):
    # Take inputs for n, c, and d
    n, c, d = map(int, input().split())

    # Take input for the list of coins and sort in descending order
    A = sorted(list(map(int, input().split())), reverse=True)

    # Check for "Infinity" and "Impossible" conditions
    if sum(A[:d]) >= c:
        print("Infinity")
    elif A[0] * d < c:
        print("Impossible")
    else:
        # Perform binary search to find the maximum number of coins that can be selected
        l, r = 1, n
        while l < r:
            mid = (l + r + 1) // 2
            coin_sum = sum(A[:mid])
            max_groups = d // (mid + 1)
            remaining_coins = d % (mid + 1)
            total_value = coin_sum * max_groups + sum(A[:remaining_coins])
            if total_value >= c:
                l = mid
            else:
                r = mid - 1

        # Print the maximum number of coins that can be selected
        print(l)
