
def find_max_diff(t: int, tests: List[Tuple[int, List[int]]]) -> None:
    for n, s in tests:
        max1_idx = s.index(max(s))
        max2_idx = s.index(sorted(s)[-2])
        
        for i in range(n):
            if i == max1_idx:
                print(max(s) - s[i])
            else:
                print(sorted(s)[-2] - s[i])
