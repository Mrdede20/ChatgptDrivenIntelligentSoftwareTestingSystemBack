
def solve(lst):
    indices = {}
    for i, num in enumerate(lst):
        if num not in indices:
            indices[num] = []
        indices[num].append(i)
    
    # Checking for Winning Pairs
    for num, idxs in indices.items():
        if len(idxs) > 1:
            if idxs[-1] - idxs[0] > 1:
                return True
    
    return False

# Main Program
t = int(input())
for _ in range(t):
    lst = list(map(int, input().split()))
    if solve(lst):
        print("YES")
    else:
        print("NO")
