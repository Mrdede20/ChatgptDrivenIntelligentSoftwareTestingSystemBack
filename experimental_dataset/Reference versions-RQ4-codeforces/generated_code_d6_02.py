
def solve(L):
    n = len(L)
    count = 0
    last = -1
    for i in range(n-1):
        if L[i] > L[i+1]:
            count += 1
            last = i
        if count > 1:
            return "NO"
    if count == 0:
        return "NO"
    if count == 1 and (last == 0 or last == n-2 or L[last-1] > L[last+1] or L[last] > L[last+2]):
        return "YES"
    else:
        return "NO"
