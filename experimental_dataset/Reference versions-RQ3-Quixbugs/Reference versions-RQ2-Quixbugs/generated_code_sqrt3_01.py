
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
