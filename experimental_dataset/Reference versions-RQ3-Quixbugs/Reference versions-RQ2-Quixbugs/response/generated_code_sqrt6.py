Program 1:

```python
def newton_raphson_sqrt(x, epsilon):
    approx_root = x / 2
    while abs(approx_root**2 - x) > epsilon:
        approx_root = (approx_root + x / approx_root) / 2
    return approx_root
```
Program 2:

```python
def newton_raphson_sqrt(x, epsilon):
    approx_root = x / 2
    diff = abs(approx_root**2 - x)
    while diff > epsilon:
        approx_root = (approx_root + x / approx_root) / 2
        diff = abs(approx_root**2 - x)
    return approx_root
```

Both programs implement the same Newton-Raphson method for finding the square root of a given number x within a given epsilon range. The algorithm follows the same steps for initialization, iteration, and calculation in both programs.

The only difference is in the condition for termination of the algorithm. Program 1 checks for the absolute difference between the calculated approximation and the actual value of the square root, while Program 2 stores this value in a variable and checks it in the loop condition.