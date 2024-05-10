
def calculate_differences(t: int, test_cases: list):
    for i in range(t):
        n, s = test_cases[i]
        mx = sorted(s, reverse=True)[:2]
        res = [max(mx) - x if x != max(mx) else max(mx) - sorted(mx)[0] for x in s]
        print(*res)
