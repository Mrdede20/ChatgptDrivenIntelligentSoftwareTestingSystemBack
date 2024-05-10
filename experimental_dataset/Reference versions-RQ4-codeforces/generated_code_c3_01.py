
def find_max_diff(t:int, test_cases:List[Tuple[int, List[int]]]) -> None:
    for i in range(t):
        n, s = test_cases[i]
        mx = [0,0]
        for j in range(n):
            if s[j] >= s[mx[0]]:
                mx[1] = mx[0]
                mx[0] = j
            elif s[j] >= s[mx[1]]:
                mx[1] = j
        for j in range(n):
            if j == mx[0]:
                print(abs(s[j]-s[mx[1]]), end=' ')
            else:
                print(abs(s[j]-s[mx[0]]), end=' ')
        print('\n', end='')

# Example Usage:
test_cases = [(5, [1, 2, 3, 4, 5]), (4, [7, 4, 9, 1])]
find_max_diff(2, test_cases)
