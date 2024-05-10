
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
