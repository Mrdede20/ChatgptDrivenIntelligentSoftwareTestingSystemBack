Sure, here are two solutions using the same method name and parameter type:

Solution 1:

```
def find_max_diff(t: int, tests: List[Tuple[int, List[int]]]) -> None:
    for n, s in tests:
        max1, max2 = float('-inf'), float('-inf')
        max1_idx, max2_idx = -1, -1

        for i in range(n):
            curr = s[i]
            if curr >= max1:
                max2 = max1
                max2_idx = max1_idx
                max1 = curr
                max1_idx = i
            elif curr > max2:
                max2 = curr
                max2_idx = i
        
        for i in range(n):
            if i == max1_idx:
                print(max2 - s[i])
            else:
                print(max1 - s[i])
```

Solution 2:

```
def find_max_diff(t: int, tests: List[Tuple[int, List[int]]]) -> None:
    for n, s in tests:
        max1_idx = s.index(max(s))
        max2_idx = s.index(sorted(s)[-2])
        
        for i in range(n):
            if i == max1_idx:
                print(max(s) - s[i])
            else:
                print(sorted(s)[-2] - s[i])
```

Both functions take in an integer `t` and a list of tuples containing an integer `n` and a list of integers `s`. They both iterate over each test case and find the indices and values of the two maximum integers in the list `s`. Finally, they iterate over the list `s` again and print the differences between each element and the maximum values.