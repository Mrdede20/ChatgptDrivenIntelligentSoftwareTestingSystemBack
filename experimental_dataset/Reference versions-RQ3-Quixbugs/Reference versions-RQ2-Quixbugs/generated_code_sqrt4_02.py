
def newton_sqrt(x, epsilon):
    """
    Computes the square root of a given floating-point number 'x'
    with an accuracy up to a tolerance level 'epsilon' using the 
    Newton-Raphson method.
    
    Parameters:
    x (float): The number to find the square root of
    epsilon (float): The tolerance level
    
    Returns:
    Approximation (float): The square root of the given number 'x'
    
    Example:
    newton_sqrt(9, 0.0001) -> 3.00009155413138
    """
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    approximation = x/2
    while True:
        difference = x - approximation**2
        if abs(difference) < epsilon:
            break
        approximation += difference/(2*approximation)
    return approximation
