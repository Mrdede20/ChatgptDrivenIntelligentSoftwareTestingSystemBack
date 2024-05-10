
def find_absolute_differences(t: int) -> None:
    for i in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        mx1 = max(s)
        mx1_index = s.index(mx1)
        s[mx1_index] = -1
        mx2 = max(s)
        for j in range(n):
            if j != mx1_index:
                print(abs(s[j] - mx1), end=' ')
            else:
                print(abs(s[j] - mx2), end=' ')
        print()

find_absolute_differences(2)  # Example input with 2 test cases
