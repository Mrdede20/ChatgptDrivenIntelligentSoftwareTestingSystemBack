
def find_max_diff(t: int, tests: List[Tuple[int, List[int]]]) -> None:
    for n, s in tests:
        max1, max2 = float('-inf'), float('-inf')
        max1_idx, max2_idx = -1, -1

        for i in range(n):
            curr = s[i]
            if curr >= max1:
                max2 = max1
                max2_idx = max1_idx
                max1 = curr
                max1_idx = i
            elif curr > max2:
                max2 = curr
                max2_idx = i
        
        for i in range(n):
            if i == max1_idx:
                print(max2 - s[i])
            else:
                print(max1 - s[i])
