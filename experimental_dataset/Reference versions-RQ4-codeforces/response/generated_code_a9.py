Here are two Python programs which achieve the given intention:

Program 1:

```python
def test_cases(t: int):
    for i in range(t):
        numbers = list(map(int, input().split()))
        numbers.sort()
        print(numbers[1])
        t -= 1
```

Program 2:

```python
def test_cases(t: int):
    while t > 0:
        numbers = list(map(int, input().split()))
        numbers.sort()
        print(numbers[1])
        t -= 1
```

Both programs take in a parameter `t` (the number of test cases) and read in three integers for each test case, sorting them in ascending order and printing the second element of the sorted list. The main difference between the programs is the loop structure used to iterate through the test cases. The first program uses a `for` loop to iterate while the second program uses a `while` loop.