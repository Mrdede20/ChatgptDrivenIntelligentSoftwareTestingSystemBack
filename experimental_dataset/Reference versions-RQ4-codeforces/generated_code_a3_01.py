
def find_second_smallest():
  t = int(input())
  for i in range(t):
    nums = list(map(int, input().split()))
    sorted_nums = sorted(nums)
    print(sorted_nums[1])
