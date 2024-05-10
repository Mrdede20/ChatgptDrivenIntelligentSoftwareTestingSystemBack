Sure, here are two programs that achieve the same intention:

Program 1:

```python
def find_second_smallest():
  t = int(input())
  for i in range(t):
    nums = list(map(int, input().split()))
    sorted_nums = sorted(nums)
    print(sorted_nums[1])
```

Program 2:

```python
def find_second_smallest():
  t = int(input())
  for i in range(t):
    nums = list(map(int, input().split()))
    smallest = float('inf')
    second_smallest = float('inf')
    for num in nums:
      if num < smallest:
        second_smallest = smallest
        smallest = num
      elif num < second_smallest:
        second_smallest = num
    print(second_smallest)
```

Both programs have the same method name `find_second_smallest` and same parameter type (no parameters). They take an integer input `t` for the number of test cases, followed by `t` lines of integer inputs. In the first program, the inputs are sorted using the `sorted` function and the second-smallest value is printed. In the second program, the inputs are iterated through and the smallest and second-smallest values are tracked using variables, and the second-smallest value is printed.