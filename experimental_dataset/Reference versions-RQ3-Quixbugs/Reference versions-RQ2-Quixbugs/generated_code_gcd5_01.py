
def gcd(a: int, b: int) -> int:
    """
    Returns the greatest common divisor (GCD) of two non-negative integers a and b.
    
    Preconditions:
        a and b are non-negative integers
    
    Example Usage:
        gcd(10, 25) -> 5
        
    """
    if b == 0:
        return a
    return gcd(b, a % b)
