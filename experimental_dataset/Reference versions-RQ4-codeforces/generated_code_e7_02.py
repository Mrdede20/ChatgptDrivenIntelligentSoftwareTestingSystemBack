
import sys

class Solution:
    def BinaryInversions(self, n: int, bits: List[int]) -> int:
        inversions = 0
        for i in range(n):
            for j in range(i+1, n):
                if bits[i] > bits[j]:
                    inversions += 1
        
        max_inv_removed = 0
        for i in range(n):
            for j in range(i+1, n):
                if bits[i] != bits[j]:
                    bits[i], bits[j] = bits[j], bits[i]
                    count_inv = 0
                    for k in range(n):
                        for l in range(k+1, n):
                            if bits[k] > bits[l]:
                                count_inv += 1
                    max_inv_removed = max(max_inv_removed, inversions - count_inv)
                    bits[i], bits[j] = bits[j], bits[i]
        
        return max_inv_removed

if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        bits = list(map(int, sys.stdin.readline().strip().split()))
        sol = Solution()
        res = sol.BinaryInversions(n, bits)
        sys.stdout.write(str(res) + "\n")
