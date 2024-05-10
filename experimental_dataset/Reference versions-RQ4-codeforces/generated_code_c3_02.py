
def find_max_diff(t:int, test_cases:List[Tuple[int, List[int]]]) -> None:
    for i in range(t):
        n, s = test_cases[i]
        mx1 = max(s)
        idx1 = s.index(mx1)
        s[idx1] = -1
        mx2 = max(s)
        idx2 = s.index(mx2)
        s[idx1] = mx1
        for j in range(n):
            if j == idx1:
                print(abs(s[j]-mx2), end=' ')
            else:
                print(abs(s[j]-mx1), end=' ')
        print('\n', end='')

# Example Usage:
test_cases = [(5, [1, 2, 3, 4, 5]), (4, [7, 4, 9, 1])]
find_max_diff(2, test_cases)
