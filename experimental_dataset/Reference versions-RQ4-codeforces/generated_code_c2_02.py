
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
        for i in s:
            if s.index(i) == mx[0]:
                print(abs(i-s[mx[1]]))
            else:
                print(abs(i-s[mx[0]]))
