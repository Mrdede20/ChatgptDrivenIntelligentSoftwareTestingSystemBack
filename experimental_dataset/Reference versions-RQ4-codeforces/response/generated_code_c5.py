Sure, here are the two programs using the same method name and parameter type:

Program 1:

```
def calculate_differences(t: int, test_cases: list):
    for i in range(t):
        n, s = test_cases[i]
        mx = sorted(s, reverse=True)[:2]
        res = [max(mx) - x if x != max(mx) else max(mx) - sorted(mx)[0] for x in s]
        print(*res)
```
Program 2:

```
def calculate_differences(t: int, test_cases: list):
    for i in range(t):
        n, s = test_cases[i]
        mx = max(s)
        mx2 = max(x for x in s if x != mx)
        res = [mx - x if x != mx else mx - mx2 for x in s]
        print(*res)
```

Both programs take an integer `t` representing the number of test cases as well as a list `test_cases` which contains `t` tuples. Each tuple contains an integer `n` representing the size of the list `s` and a list `s` of `n` integers. 

The program iterates over each test case and finds the two maximum elements of the list `s`. It then calculates the differences between each element in the list and the smaller of the two maximum elements, and stores the results in a list `res`. Finally, the program prints out the list `res` on a new line for each test case.