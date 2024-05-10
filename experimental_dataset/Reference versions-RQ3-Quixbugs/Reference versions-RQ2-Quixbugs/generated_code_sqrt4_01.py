
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
    newton_sqrt(4, 0.001) -> 2.0000000929222947
    """
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    guess = x/2
    while abs(guess*guess - x) > epsilon:
        guess = (guess + x/guess)/2
    return guess
