input = __import__('sys').stdin.readline

for _ in range(int(input())):
    n, c, d = map(int, input().split())
    a = sorted([*map(int, input().split())], reverse=True)

    if sum(a[:min(d, len(a))]) >= c:
        print('Infinity')
        continue

    if a[0] * d < c:
        print('Impossible')
        continue

    psum = [0] * (n + 1)
    for i in range(1, n+1):
        psum[i] = psum[i-1] + a[i-1]

    l, r = 0, d
    while l + 1 < r:
        mid = (l + r) // 2 + 1

        if mid >= n:
            value = psum[-1] * (d // mid)
            if d % mid:
                value += psum[min(n, d % mid)]
        else:
            value = psum[mid] * (d // mid)
            if d % mid:
                value += psum[d % mid]

        if value >= c: l = mid - 1
        else: r = mid - 1

    print(l)