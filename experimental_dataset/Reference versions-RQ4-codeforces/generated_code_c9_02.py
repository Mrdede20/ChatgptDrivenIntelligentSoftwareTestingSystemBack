
def find_differences(t: int, test_cases: list):
    for i in range(t):
        n, s = test_cases[i]
        largest = max(s)
        second_largest = max(c for c in s if c != largest)
        for item in s:
            print(abs(largest-item), abs(second_largest-item))
