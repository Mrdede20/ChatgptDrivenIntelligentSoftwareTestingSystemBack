
def gcd(a: int, b: int) -> int:
    """
    Returns the greatest common divisor (GCD) of two non-negative integers a and b.
    
    Preconditions:
        a and b are non-negative integers
    
    Example Usage:
        gcd(12, 18) -> 6
        
    """
    if a == 0:
        return b
    return gcd(b%a, a)
