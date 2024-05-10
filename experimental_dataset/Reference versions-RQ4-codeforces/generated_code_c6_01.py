
def find_absolute_differences(t: int) -> None:
    for i in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        mx = [-1, -1]
        for j in range(n):
            if mx[0] == -1 or s[j] > s[mx[0]]:
                mx[1] = mx[0]
                mx[0] = j
            elif mx[1] == -1 or s[j] > s[mx[1]]:
                mx[1] = j
        for j in range(n):
            if j != mx[0]:
                print(abs(s[j] - s[mx[0]]), end=' ')
            else:
                print(abs(s[j] - s[mx[1]]), end=' ')
        print()

find_absolute_differences(2)  # Example input with 2 test cases
