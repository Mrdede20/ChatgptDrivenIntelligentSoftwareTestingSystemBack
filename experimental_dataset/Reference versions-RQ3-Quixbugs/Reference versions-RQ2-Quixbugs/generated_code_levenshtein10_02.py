
def levenshtein_distance(s, t):
    """
    Calculates the Levenshtein Distance between two strings s and t using recursion and memoization.

    Args:
        s (str): The source string.
        t (str): The destination string.

    Returns:
        int: The minimum number of single-character edits needed to transform s into t.
    """
    memo = {}
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(s):
            memo[(i, j)] = len(t) - j
        elif j == len(t):
            memo[(i, j)] = len(s) - i
        elif s[i] == t[j]:
            memo[(i, j)] = helper(i+1, j+1)
        else:
            deletion = helper(i+1, j)
            insertion = helper(i, j+1)
            substitution = helper(i+1, j+1)
            memo[(i, j)] = 1 + min(deletion, insertion, substitution)
        return memo[(i, j)]
    return helper(0, 0)
