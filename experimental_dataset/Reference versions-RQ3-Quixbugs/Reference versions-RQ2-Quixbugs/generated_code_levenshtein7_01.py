
def levenshtein_distance(s1, s2):
    # If either string is empty, return the length of the non-empty string
    if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    
    # If the first characters match, recursion with remaining part
    if s1[0] == s2[0]:
        return levenshtein_distance(s1[1:], s2[1:])
    
    # Recursion to calculate distance for each of the three different operations
    remove_dist = levenshtein_distance(s1, s2[1:])
    add_dist = levenshtein_distance(s1[1:], s2)
    change_dist = levenshtein_distance(s1[1:], s2[1:])
    
    # Return the minimum of the three distances plus 1 (the cost of the operation)
    return 1 + min(remove_dist, add_dist, change_dist)
