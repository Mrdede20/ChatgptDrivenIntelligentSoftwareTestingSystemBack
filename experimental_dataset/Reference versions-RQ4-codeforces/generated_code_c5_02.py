
def calculate_differences(t: int, test_cases: list):
    for i in range(t):
        n, s = test_cases[i]
        mx = max(s)
        mx2 = max(x for x in s if x != mx)
        res = [mx - x if x != mx else mx - mx2 for x in s]
        print(*res)
