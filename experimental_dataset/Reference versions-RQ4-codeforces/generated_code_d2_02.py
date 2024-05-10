
def solve(n, arr):
    valleys = []

    for i in range(1, n-1):
        if arr[i-1] > arr[i] and arr[i+1] > arr[i]:
            valleys.append(i)

    if len(valleys) != 1:
        return False

    start = valleys[0]
    end = start

    while end < n-1:
        if arr[end+1] < arr[end]:
            break

        end += 1

    if end == n-1 or end == start:
        return False

    while end < n-1:
        if arr[end+1] > arr[end]:
            break

        end += 1

    return end == n-1

tests = int(input())

for t in range(tests):
    n = int(input())
    arr = list(map(int, input().split()))

    if solve(n, arr):
        print('YES')
    else:
        print('NO')
