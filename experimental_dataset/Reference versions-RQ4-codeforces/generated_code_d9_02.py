
from bisect import bisect

def find_valleys(mountains):
    valleys = []
    for i, height in enumerate(mountains):
        if i == 0:
            if height < mountains[i+1]:
                valleys.append(i)
        elif i == len(mountains) - 1:
            if height < mountains[i-1]:
                valleys.append(i)
        else:
            if height < mountains[i-1] and height < mountains[i+1]:
                valleys.append(i)
                
    return valleys

def has_contiguous_sublist(mountains):
    valleys = find_valleys(mountains)
    if len(valleys) < 2:
        return False
    
    for i in range(len(valleys) - 1):
        left = bisect(mountains, mountains[valleys[i]], 0, valleys[i]+1)
        right = bisect(mountains, mountains[valleys[i]], valleys[i]+1)
        if valleys[i+1] in range(left, right):
            return True
        
    return False
