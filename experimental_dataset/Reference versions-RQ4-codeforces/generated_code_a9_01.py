
def test_cases(t: int):
    for i in range(t):
        numbers = list(map(int, input().split()))
        numbers.sort()
        print(numbers[1])
        t -= 1
