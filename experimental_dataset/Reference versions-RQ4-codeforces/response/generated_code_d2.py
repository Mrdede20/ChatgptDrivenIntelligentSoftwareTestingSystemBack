Here are two programs that solve the problem using different approaches:

Program 1:

```
def solve(n, arr):
    valleys = []

    for i in range(1, n-1):
        if arr[i-1] > arr[i] and arr[i+1] > arr[i]:
            valleys.append(i)

    if len(valleys) != 1:
        return False

    start = valleys[0]
    end = start

    while end < n-1 and arr[end+1] < arr[end]:
        end += 1

    if end == n-1 or end == start:
        return False

    while end < n-1 and arr[end+1] > arr[end]:
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
```

Program 2:

```
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
```

Both programs take the same input and have the same function signature `def solve(n, arr)`. They iterate through the array and look for valleys. If only one valley is found, they check if it can be used to split the array into strictly increasing and strictly decreasing sequences. If so, they return True, otherwise they return False. The two programs differ in the way they iterate through the array to find the end of the strictly increasing and strictly decreasing sequences. Program 1 uses the `arr[end+1] < arr[end]` and `arr[end+1] > arr[end]` conditions in `while` loops, while Program 2 uses `if` statements inside the loops to achieve the same effect.