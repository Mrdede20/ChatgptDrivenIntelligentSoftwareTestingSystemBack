Program 1:

```python
def find_absolute_diff(t:int):
    for i in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        mx = [0, 0]
        for i in range(n):
            if s[i] > s[mx[0]]:
                mx[1] = mx[0]
                mx[0] = i
            elif s[i] > s[mx[1]] and s[i] != s[mx[0]]:
                mx[1] = i
        for i in range(n):
            if i == mx[0]:
                print(abs(s[i]-s[mx[1]]))
            else:
                print(abs(s[i]-s[mx[0]]))
```

Program 2:

```python
def find_absolute_diff(t:int):
    for i in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        mx = [0, 0]
        for i in range(n):
            if s[i] > s[mx[0]]:
                mx[1] = mx[0]
                mx[0] = i
            elif s[i] > s[mx[1]] and s[i] != s[mx[0]]:
                mx[1] = i
        for i in s:
            if s.index(i) == mx[0]:
                print(abs(i-s[mx[1]]))
            else:
                print(abs(i-s[mx[0]]))
```

Both programs take `t` as an integer which represents the number of test cases. For each test case, they take an integer `n` which represents the number of elements in the next input line. The next line contains `n` space-separated integers which are stored in a list `s`. 

The code then finds the two indices (stored in `mx`) from the list `s` such that the elements at those indices have the highest and second highest values respectively. 

Finally, the code loops through each element in the list `s` and calculates the difference between the element and the highest element and prints it (for the highest element) or the difference between the element and the second highest element and prints it (for the other elements). 

The purpose of this code is to calculate the absolute difference between each element in the list and the highest or second highest element in the list.