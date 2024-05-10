Sure, here are two versions of the program:

Version 1:

```python
def second_largest(t: int) -> None:
    for i in range(t):
        a, b, c = sorted(map(int, input().split()))
        print(b)
```

Version 2:

```python
def second_largest(t: int) -> None:
    for i in range(t):
        nums = list(map(int, input().split()))
        nums.remove(max(nums))
        print(max(nums))
```

Both of these functions take an integer `t` as input, which represents the number of test cases. They then iterate over `t` test cases, taking three integers as input and sorting them. 

In version 1, the sorted integers are assigned to variables `a`, `b`, and `c`, and the second largest value (`b`) is printed.

In version 2, the integers are stored in a list called `nums`, and the maximum value is removed from the list using the `remove()` method. The maximum of the new list is then printed, which is the second largest value.  

Note that both versions assume that the input integers are separated by whitespace.