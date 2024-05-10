Here's the first program to achieve the intention:

```python
def find_middle(t):
    while t != 0:
        a, b, c = map(int, input().split())
        arr = [a, b, c]
        arr.sort()
        print(arr[1])
        t -= 1
```

This program takes the number of test cases as input and then runs a loop until all the test cases are completed. Within the loop, it takes input for each test case, sorts the three numbers in ascending order and then prints the middle number. Once all the test cases are processed, the loop stops and the program ends.

Here's the second program to achieve the same intention:

```python
def find_middle(t):
    for i in range(t):
        a, b, c = map(int, input().split())
        arr = [a, b, c]
        arr.sort()
        print(arr[1])
```

This program uses a for loop to iterate through each test case, takes input for each test case, sorts the three numbers in ascending order and then prints the middle number. Once all the test cases are processed, the loop stops and the program ends.