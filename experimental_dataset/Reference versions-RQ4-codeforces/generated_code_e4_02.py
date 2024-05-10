
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
