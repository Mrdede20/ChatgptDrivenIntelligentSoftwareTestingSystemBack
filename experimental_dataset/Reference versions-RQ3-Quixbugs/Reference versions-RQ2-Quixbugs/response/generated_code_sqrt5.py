Program 1:

```python
def calculate_sqrt(x, epsilon):
    approx = x/2
    while abs(approx**2 - x) > epsilon:
        approx = (approx + x/approx)/2
    return approx
```

Program 2 (optimized using math.isclose()):

```python
import math

def calculate_sqrt(x, epsilon):
    approx = x/2
    while not math.isclose(approx**2, x, rel_tol=epsilon):
        approx = (approx + x/approx)/2
    return approx
```

Both of these programs achieve the same goal of calculating the square root of a positive float number using the Newton-Raphson method with a given precision. The first program uses a simple absolute value comparison to check if the difference between the current approximation and the actual square root is less than the given epsilon, while the second program uses the built-in math.isclose() function to make a relative comparison with a given relative tolerance. The second program is more optimized in terms of precision handling as it takes care of machine precision errors, but the first program can also give the desired results within an acceptable margin of error.