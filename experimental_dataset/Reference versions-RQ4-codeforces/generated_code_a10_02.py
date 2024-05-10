
def second_smallest(t: int) -> None:
    while t > 0:
        nums = list(map(int, input().split()))
        nums.sort()
        print(nums[1])
        t -= 1
