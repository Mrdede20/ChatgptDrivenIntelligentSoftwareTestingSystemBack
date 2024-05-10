t = int(input())

for _ in range(t):
    n, c, d = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    if sum(A[:d]) >= c:
        print("Infinity")
        continue
    elif A[0] * d < c:
        print("Impossible")
        continue

    l, r = 1, d
    while l < r:
        mid = (l + r + 1) // 2
        total_value = sum(A[:mid]) * (d // (mid) ) + sum(A[:d % mid])
        if total_value >= c:
            l = mid
        else:
            r = mid - 1

    print(l-1)
