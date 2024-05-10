Here's one possible implementation of the program:

```
import sys

class Solution:
    def BinaryInversions(self, n, bits):
        ones_count = bits.count(1)
        inversions = ones_count * (n - ones_count)
        return inversions

solution = Solution()

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    bits = list(map(int, sys.stdin.readline().split()))
    result = solution.BinaryInversions(n, bits)
    print(result)
```

Here's another implementation using list comprehensions:

```
import sys

class Solution:
    def BinaryInversions(self, n, bits):
        ones = [i for i in range(n) if bits[i] == 1]
        zeros = [i for i in range(n) if bits[i] == 0]
        inversions = sum([len(zeros) - j for j in range(len(ones))])
        return inversions

solution = Solution()

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    bits = list(map(int, sys.stdin.readline().split()))
    result = solution.BinaryInversions(n, bits)
    print(result)
```