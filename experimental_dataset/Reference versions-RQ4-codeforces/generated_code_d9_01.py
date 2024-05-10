
from bisect import bisect_left, bisect_right

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
        if valleys[i+1] - valleys[i] > 1:
            return True
        
    return False
