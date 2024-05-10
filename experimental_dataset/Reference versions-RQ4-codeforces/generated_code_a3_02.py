
def find_second_smallest():
  t = int(input())
  for i in range(t):
    nums = list(map(int, input().split()))
    smallest = float('inf')
    second_smallest = float('inf')
    for num in nums:
      if num < smallest:
        second_smallest = smallest
        smallest = num
      elif num < second_smallest:
        second_smallest = num
    print(second_smallest)
