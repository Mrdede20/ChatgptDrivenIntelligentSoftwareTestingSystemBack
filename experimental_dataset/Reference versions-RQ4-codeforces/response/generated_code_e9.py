Here are two Python programs that achieve this intention using the same method name and parameter type:

Program 1:
```python
def find_max_inversions(test_cases: int, binary_strings: List[str]) -> List[int]:
    max_inversions = []
    for i in range(test_cases):
        n = len(binary_strings[i])
        count_1 = 0
        count_0 = 0
        for j in range(n):
            if binary_strings[i][j] == '1':
                count_1 += 1
                max_inversions.append(count_0)
            else:
                count_0 += 1
        max_inversions.append(count_1)
        if len(max_inversions) == n+1:
            max_inversions.pop()
    return max_inversions
```
Program 2:
```python
def find_max_inversions(test_cases: int, binary_strings: List[str]) -> List[int]:
    max_inversions = []
    for i in range(test_cases):
        n = len(binary_strings[i])
        count_1 = 0
        count_0 = 0
        for j in range(n):
            if binary_strings[i][j] == '0':
                count_0 += 1
                max_inversions.append(count_1)
            else:
                count_1 += 1
        max_inversions.append(count_0)
        if len(max_inversions) == n+1:
            max_inversions.pop()
    return max_inversions
```
Both programs take in an integer `test_cases` and a list `binary_strings` containing the binary strings corresponding to each test case. The function returns a list containing the maximum number of inversions made to each binary string.

Program 1 works by counting the number of 1's and 0's encountered while iterating through the binary string. When a 1 is encountered, the count of 0's is appended to the `max_inversions` list. When a 0 is encountered, the count of 1's is not appended since it does not represent a valid flip. The final count of 1's is appended to the list as well.

Program 2 works in a similar fashion, except the count of 1's and 0's is swapped. When a 0 is encountered, the count of 1's is appended since flipping two 0's does not result in a valid flip. When a 1 is encountered, the count of 0's is not appended. The final count of 0's is appended instead.