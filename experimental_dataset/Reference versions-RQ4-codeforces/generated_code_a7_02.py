
def second_largest(t: int) -> None:
    for i in range(t):
        nums = list(map(int, input().split()))
        nums.remove(max(nums))
        print(max(nums))
