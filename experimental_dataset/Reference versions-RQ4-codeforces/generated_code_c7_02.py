
from typing import List, Tuple

def find_diff(t: int, test_cases: List[Tuple[int, List[int]]]) -> List[List[int]]:
    result = []
    for i in range(t):
        n, s = test_cases[i]
        sorted_array = sorted(s,reverse=True)
        max1 = sorted_array[0]
        max2 = sorted_array[1]
        temp = []
        for j in range(n):
            if s[j] == max1:
                temp.append(abs(max2 - s[j]))
            else:
                temp.append(abs(max1 - s[j]))
        result.append(temp)
    return result
