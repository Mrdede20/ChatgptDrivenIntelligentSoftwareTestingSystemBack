
def find_absolute_diff(t:int):
    for i in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        mx = [0, 0]
        for i in range(n):
            if s[i] > s[mx[0]]:
                mx[1] = mx[0]
                mx[0] = i
            elif s[i] > s[mx[1]] and s[i] != s[mx[0]]:
                mx[1] = i
        for i in range(n):
            if i == mx[0]:
                print(abs(s[i]-s[mx[1]]))
            else:
                print(abs(s[i]-s[mx[0]]))
