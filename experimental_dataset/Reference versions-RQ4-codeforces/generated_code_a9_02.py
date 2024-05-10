
def test_cases(t: int):
    while t > 0:
        numbers = list(map(int, input().split()))
        numbers.sort()
        print(numbers[1])
        t -= 1
