
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
