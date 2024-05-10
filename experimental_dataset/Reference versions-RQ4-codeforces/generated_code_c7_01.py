
def find_diff(t: int, test_cases: List[Tuple[int, List[int]]]) -> List[List[int]]:
  result = []
  for i in range(t):
    n, s = test_cases[i]
    max1 = max2 = s[0]
    for j in range(1, n):
      if s[j] > max1:
        max2 = max1
        max1 = s[j]
      elif s[j] > max2:
        max2 = s[j]
    temp = []
    for j in range(n):
      if s[j] == max1:
        temp.append(abs(max2 - s[j]))
      else:
        temp.append(abs(max1 - s[j]))
    result.append(temp)
  return result
