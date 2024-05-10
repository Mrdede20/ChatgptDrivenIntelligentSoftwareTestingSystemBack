
from typing import List

def valleys_exist(towers: List[int]) -> str:
    valleys = []
    for i in range(1, len(towers)-1):
        if towers[i-1] > towers[i] < towers[i+1]:
            j = i-1
            while j >= 0 and towers[j] > towers[j+1]:
                j -= 1
            k = i+1
            while k < len(towers) and towers[k] > towers[k-1]:
                k += 1
            valleys.append((j+1, k-1))
    for i in range(len(valleys)):
        for j in range(i+1, len(valleys)):
            if set(range(*valleys[i])) & set(range(*valleys[j])):
                return "YES"
    return "NO"
