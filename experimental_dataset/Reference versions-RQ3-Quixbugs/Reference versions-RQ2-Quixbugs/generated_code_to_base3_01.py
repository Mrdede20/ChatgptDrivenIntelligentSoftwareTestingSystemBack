
def to_base(num: int, b: int) -> str:
    """
    Converts an integer from base 10 to base b.

    Args:
        num: An integer to convert to base b.
        b: The desired base to convert to.

    Returns:
        A string representing num in base b.

    Preconditions:
        num >= 0
        2 <= b <= 36
    """
    result = ''

    # Define string of characters to use as placeholders
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Convert num to base b
    while num > 0:
        i = num % b
        num //= b
        result = alphabet[i] + result

    return result


# Example call
print(to_base(123, 16))  # Output: "7B"
