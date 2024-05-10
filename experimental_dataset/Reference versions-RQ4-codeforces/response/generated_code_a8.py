Here are two possible Python programs that achieve the intended functionality:

Program 1:
```python
def sort_and_print_middle(t: int) -> None:
    while t > 0:
        a, b, c = map(int, input().split())
        lst = [a, b, c]
        lst.sort()
        print(lst[1])
        t -= 1
```

Program 2:
```python
def sort_and_print_middle(t: int) -> None:
    for i in range(t):
        a, b, c = map(int, input().split())
        if b <= a <= c or c <= a <= b:
            print(a)
        elif a <= b <= c or c <= b <= a:
            print(b)
        else:
            print(c)
```

Both programs take an integer parameter t representing the number of test cases. They both iterate through t test cases, taking three integers a, b, and c as input for each test case. They then sort the three integers in ascending order and print the middle value (second element in the sorted list). The first program achieves this using the sort() method, while the second program achieves this using conditional statements to find the middle value.