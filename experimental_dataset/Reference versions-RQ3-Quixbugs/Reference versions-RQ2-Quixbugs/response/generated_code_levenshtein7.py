Sure, here are two implementations:

Implementation 1:
```
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
```

Implementation 2:
```
def levenshtein_distance(s1, s2):
    # Initialize a 2D table to hold minimum distances
    table = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    
    # Base cases
    for i in range(len(s1) + 1):
        table[i][0] = i
    for j in range(len(s2) + 1):
        table[0][j] = j
    
    # Fill in the table using dynamic programming
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
    
    # Return the final minimum distance
    return table[len(s1)][len(s2)]
``` 

Both implementations should work correctly and have O(mn) time complexity, where m and n are the lengths of the two strings. The first implementation is a recursive solution and the second implementation is a dynamic programming solution that builds a table to store intermediate results. The dynamic programming approach is generally more efficient for longer strings, while the recursive approach is more straightforward to understand.