
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
    # Step 1: Initialize an empty string result.
    result = ''

    # Step 2: Create a string of characters alphabet.
    # Use string.ascii_uppercase and string.digits to get upper case letters and digits respectively
    import string
    alphabet = string.digits + string.ascii_uppercase

    # Step 3: Perform repeated division and concatenation until num is 0.
    while num > 0:
        # Take the remainder of num divided by b.
        i = num % b
        
        # Divide num by b, discard the remainder, and store the quotient back into num.
        num //= b
        
        # Lookup the character in the alphabet string at the index i, and concatenate it onto the beginning of result.
        result = alphabet[i] + result

    # Step 4: Return the result string
    return result


# Example call
print(to_base(123, 16))  # Output: "7B"
