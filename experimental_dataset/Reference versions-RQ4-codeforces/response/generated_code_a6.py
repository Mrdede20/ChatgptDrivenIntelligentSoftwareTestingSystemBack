Sure, here are two programs that achieve the same intention:

Program 1:
```python
def second_smallest(t:int)->None:
    for _ in range(t):
        nums = list(map(int, input().split()))
        nums.sort()
        print(nums[1])
```

Program 2:
```python
def second_smallest(t:int)->None:
    for _ in range(t):
        a, b, c = map(int, input().split())
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        print(b)
```
Both programs take an integer `t` as input, which represents the number of test cases. They then iterate through each test case, taking 3 integers as input, sorting them in ascending order, and finally outputting the second smallest integer.

In the second program, instead of using the `sort()` function, we use a series of conditional statements to compare and swap numbers, ultimately finding the second largest of the three.