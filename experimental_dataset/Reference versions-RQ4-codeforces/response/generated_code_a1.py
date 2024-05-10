Sure, here are two implementations of the same program:

Implementation 1:
```python
def print_second_smallest(t):
    for i in range(t):
        lst = list(map(int, input().split()))
        lst.remove(max(lst))
        print(min(lst))
```

In the above code, we are using a for loop to iterate through the test cases t. We are then taking input of three integers at a time and storing them in the list "lst". We remove the maximum value from the list using the remove() method, which leaves us with two integers, and we print the second smallest integer using the min() function.

Implementation 2:
```python
def print_second_smallest(t):
    while t > 0:
        a, b, c = map(int, input().split())
        if a > b:
            if c > b:
                print(c)
            elif a > c:
                print(a)
            else:
                print(c)
        else:
            if c > a:
                print(c)
            elif b > c:
                print(b)
            else:
                print(c)
        t -= 1
```

In the above code, we are using a while loop to iterate through the test cases t. We are taking input of three integers at a time and storing them in variables a, b, and c. We are then using a series of if-else statements to check which integer is the second smallest and print that integer. This implementation is a bit longer and more complex than the first one, but it is more efficient in terms of time complexity as we are not using any list or memory to store the input values.