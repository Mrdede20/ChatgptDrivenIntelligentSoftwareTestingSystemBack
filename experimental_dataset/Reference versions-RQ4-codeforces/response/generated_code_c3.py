Program 1:

```python
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
```

Program 2:

```python
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
```

Both programs take in the same parameters:
- `t` (int) - number of test cases
- `test_cases` (List[Tuple[int, List[int]]]) - a list of tuples, where each tuple represents a test case. The first element of the tuple is an integer `n` (number of integers in the list), and the second element is a list `s` of `n` integers.

Both programs output the same result, as described in the problem statement. The first program makes use of a `mx` list to store the indices of the two maximum values, while the second program makes use of the `index()` method to find the indices directly.