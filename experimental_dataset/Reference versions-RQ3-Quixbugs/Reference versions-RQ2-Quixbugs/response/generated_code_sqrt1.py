Sure, here are two programs using the Newton-Raphson method to calculate the square root with a certain level of tolerance:

Program 1:

```
def newton_raphson_square_root(x, epsilon):
    approx = x / 2.0
    while True:
        better_approx = (approx + x / approx) / 2.0
        if abs(better_approx - approx) < epsilon:
            return better_approx
        approx = better_approx
```

Program 2:

```
def newton_raphson_square_root(x, epsilon):
    approx = x / 2.0
    difference = abs(x - approx**2)
    while difference > epsilon:
        approx = (approx + x / approx) / 2.0
        difference = abs(x - approx**2)
    return approx
```

Both programs use the same method name `newton_raphson_square_root` and have the same parameter types: a float value (`x`) and a tolerance level (`epsilon`). The first program uses a `while True` loop to iterate until reaching the desired level of accuracy, while the second program uses a `while` loop to iterate until the difference between the current approximation and the actual value is less than the given tolerance.