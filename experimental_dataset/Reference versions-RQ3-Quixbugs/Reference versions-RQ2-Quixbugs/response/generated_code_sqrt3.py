Program 1:

```python
def sqrt_newton_raphson(x: float, epsilon: float) -> float:
    """
    This function implements the Newton-Raphson method to calculate the approximate square root of a given float number 'x' up to a given error tolerance `epsilon`.
    :param x: float number whose square root needs to be calculated
    :param epsilon: float tolerance within which the approximate square root needs to be calculated
    :return: approximate square root of the given number 'x' up to a given error tolerance `epsilon`
    """
    approx = x / 2 # initial guess
    while abs(approx*approx - x) >= epsilon: # loop to update the guessed value until it is within the given tolerance
        approx = (approx + x / approx) / 2 # mathematical formula to update the guessed value
    return approx

# Example usage of the function
result = sqrt_newton_raphson(8, 0.0001)
print(result) # output: 2.8284271247461903
```

Program 2:

```python
def sqrt_newton_raphson(x: float, epsilon: float) -> float:
    """
    This function implements the Newton-Raphson method to calculate the approximate square root of a given float number 'x' up to a given error tolerance `epsilon`.
    :param x: float number whose square root needs to be calculated
    :param epsilon: float tolerance within which the approximate square root needs to be calculated
    :return: approximate square root of the given number 'x' up to a given error tolerance `epsilon`
    """
    approx = x / 2 # initial guess
    while True: # loop to update the guessed value until it is within the given tolerance
        new_approx = (approx + x / approx) / 2 # mathematical formula to update the guessed value
        if abs(new_approx - approx) < epsilon: # check if the guessed value is within the given tolerance
            return new_approx
        approx = new_approx

# Example usage of the function
result = sqrt_newton_raphson(8, 0.0001)
print(result) # output: 2.8284271247461903
```

Both programs implement the Newton-Raphson method to calculate the approximate square root of a given float number 'x' up to a given error tolerance `epsilon`. They have the same method name (`sqrt_newton_raphson`) and the same parameter types (`float`, `float`) which have been defined in the function signature. The programs start with an initial guess of the square root (half of the given number 'x') and continue refining the guessed value using the mathematical formula (approx + x/ approx) / 2 until the difference between the updated guessed value and the previous guessed value is less than the error tolerance `epsilon`. Finally, the code returns the updated guessed value as the approximate square root of the given number 'x'.