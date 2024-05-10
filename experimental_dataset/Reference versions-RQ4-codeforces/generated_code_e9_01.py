
def find_max_inversions(test_cases: int, binary_strings: List[str]) -> List[int]:
    max_inversions = []
    for i in range(test_cases):
        n = len(binary_strings[i])
        count_1 = 0
        count_0 = 0
        for j in range(n):
            if binary_strings[i][j] == '1':
                count_1 += 1
                max_inversions.append(count_0)
            else:
                count_0 += 1
        max_inversions.append(count_1)
        if len(max_inversions) == n+1:
            max_inversions.pop()
    return max_inversions
