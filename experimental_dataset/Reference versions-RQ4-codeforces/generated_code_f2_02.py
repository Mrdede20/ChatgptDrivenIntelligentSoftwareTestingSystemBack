
def max_coins():
    # Step 1: Take an integer input
    t = int(input())
    
    # Iterate t times
    for i in range(t):
        # Step 2: Take inputs for n, c, d and list A
        n, c, d = map(int, input().split())
        A = sorted(map(int, input().split()), reverse=True)
        
        # Step 4: Check conditions against list A
        if A[0] > d*c:
            print("Infinity")
            continue
        if sum(A[:d]) < c:
            print("Impossible")
            continue
        
        # Step 5: Perform binary search
        l, r = 0, n
        while l < r:
            mid = (l+r+1) // 2
            # Step 6: Calculate sum and distribute among d people
            temp_sum = sum(A[:mid+1])
            coins_per_person = [temp_sum // d] * d
            for j in range(temp_sum % d):
                coins_per_person[j] += 1
            # Step 7: Calculate total number of coins earned
            total_coins = sum(min(coins_per_person[j], A[j]) for j in range(d))
            # Step 8: Update l or r based on earned coins
            if total_coins >= c:
                l = mid
            else:
                r = mid - 1
        
        # Step 9: Print maximum number of coins earned
        print(l + 1)
