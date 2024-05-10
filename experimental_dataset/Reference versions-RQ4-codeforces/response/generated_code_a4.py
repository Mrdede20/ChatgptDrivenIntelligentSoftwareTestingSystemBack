Here are two programs which achieve the same intention:

First program using basic sorting:

```python
def find_median(t: int) -> None:
    # loop for t test cases
    for i in range(t):
        # input the three integers
        a, b, c = map(int, input().split())
        # sort the integers
        arr = sorted([a, b, c])
        # print the middle integer
        print(arr[1])
```

Second program using median function from statistics module:

```python
import statistics

def find_median(t: int) -> None:
    # loop for t test cases
    for i in range(t):
        # input the three integers
        a, b, c = map(int, input().split())
        # calculate the median
        median = statistics.median([a, b, c])
        # print the median
        print(median)
```

Both programs will take an integer `t` as an input representing the number of test cases and then for each test case, the user will input three space-separated integers. The programs will then sort those three integers and print the middle integer, which is the second integer after sorting. This will be repeated until `t` becomes 1.