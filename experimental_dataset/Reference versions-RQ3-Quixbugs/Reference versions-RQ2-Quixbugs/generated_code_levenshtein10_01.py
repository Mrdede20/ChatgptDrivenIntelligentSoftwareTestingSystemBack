
def levenshtein_distance(s, t):
    """
    Calculates the Levenshtein Distance between two strings s and t using recursion.

    Args:
        s (str): The source string.
        t (str): The destination string.

    Returns:
        int: The minimum number of single-character edits needed to transform s into t.
    """
    if not s:
        return len(t)
    if not t:
        return len(s)
    if s[0] == t[0]:
        return levenshtein_distance(s[1:], t[1:])
    deletion = levenshtein_distance(s[1:], t)
    insertion = levenshtein_distance(s, t[1:])
    substitution = levenshtein_distance(s[1:], t[1:])
    return 1 + min(deletion, insertion, substitution)
