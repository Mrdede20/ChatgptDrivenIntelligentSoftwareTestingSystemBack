
def solve(L):
    n = len(L)
    for i in range(n):
        temp = L[:i] + L[i+1:]
        flag = True
        for j in range(len(temp)-1):
            if temp[j] <= temp[j+1]:
                flag = False
                break
        if flag:
            return "YES"
    return "NO"
