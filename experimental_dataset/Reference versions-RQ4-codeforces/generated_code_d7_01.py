
def solve(lst):
    valleys = []
    
    # Creating Valleys
    i = 0
    while i < len(lst):
        j = i
        while j < len(lst)-1 and lst[j] == lst[j+1]:
            j += 1
        valleys.append(lst[i:j+1])
        i = j+1
    
    # Checking for Winning Pairs
    for valley in valleys:
        pairs = []
        for i in range(len(valley)):
            for j in range(i+1, len(valley)):
                if valley[i] == valley[j]:
                    pairs.append((i,j))
        
        if len(pairs) == 1:
            a,b = pairs[0]
            if (valley.index(valley[a]) < a and valley.index(valley[b]) > b) or \
                (valley.index(valley[a]) > a and valley.index(valley[b]) < b):
                    return True
    
    return False

# Main Program
t = int(input())
for _ in range(t):
    lst = list(map(int, input().split()))
    if solve(lst):
        print("YES")
    else:
        print("NO")
