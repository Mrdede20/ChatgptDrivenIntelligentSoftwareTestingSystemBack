def has_adjacent_valley(lst):
    valleys = []
    for i in range(1, len(lst) - 1):
        if lst[i-1] > lst[i] < lst[i+1]:
            valleys.append((i-1, i, i+1))

    if len(valleys) == 1:
        return True
    else:
        return False

def read_input():
    return list(map(int, input().strip().split()))

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    lst = read_input()

    if has_adjacent_valley(lst):
        print("YES")
    else:
        print("NO")
