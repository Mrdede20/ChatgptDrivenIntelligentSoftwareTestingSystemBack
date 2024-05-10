Here are two programs that achieve the same intention:

Program 1:
```python
def print_middle_integer(t:int):
    for i in range(t):
        a, b, c = sorted(map(int, input().split()))
        print(b)
```

Program 2:
```python
def print_middle_integer(t:int):
    for i in range(t):
        lst = list(map(int, input().split()))
        lst.sort()
        print(lst[1])
```

Both programs take an integer t as input which represents the number of test cases. Then, for each test case, three integers are input and sorted using either the sorted() function or the sort() method. The second smallest integer (middle integer) is then printed using the indexing technique. This process continues until all test cases have been processed.