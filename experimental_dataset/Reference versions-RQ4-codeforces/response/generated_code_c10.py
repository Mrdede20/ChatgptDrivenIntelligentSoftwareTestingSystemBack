Program 1:

```python
def max_difference(t, n, s):
    for i in range(t):
        max1 = max2 = float('-inf')
        for num in s[i]:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        for num in s[i]:
            if num == max1:
                print(max1 - max2)
            else:
                print(max1 - num)
```

Program 2: 

```python
def max_difference(t, n, s):
    for i in range(t):
        s[i].sort(reverse=True)
        max1 = s[i][0]
        max2 = s[i][1]
        for num in s[i]:
            if num == max1:
                print(max1 - max2)
            else:
                print(max1 - num)
```

Both programs achieve the same output. The first program finds the two maximum values in the input array using a loop and conditional statements while the second program sorts the input array in descending order and picks the first two elements as the maximum values. They both then loop through the input array again to calculate and print the difference between each element and the maximum values.