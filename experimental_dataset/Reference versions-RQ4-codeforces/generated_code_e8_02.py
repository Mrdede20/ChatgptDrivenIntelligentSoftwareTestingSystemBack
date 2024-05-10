
class Solution:
    def BinaryInversions(self, n: int, bits: List[int]) -> int:
        first_one = -1
        first_zero = -1
        for i in range(n):
            if bits[i] == 1:
                first_one = i
                break
        for i in range(n):
            if bits[i] == 0:
                first_zero = i
                break
        if first_one == -1 or first_zero == -1:
            return 0
        bin1 = bits.copy()
        bin1[first_one] = 0
        bin1[first_zero] = 1
        inv1 = self.get_inversions(bits, bin1)
        bin2 = bits.copy()
        bin2[first_one], bin2[first_zero] = bin2[first_zero], bin2[first_one]
        inv2 = self.get_inversions(bits, bin2)
        return max(inv1, inv2)

    def get_inversions(self, arr1, arr2):
        n = len(arr1)
        first = [-1] * n
        for i in range(n):
            first[arr1[i]] = i
        coord = [first[arr2[i]] for i in range(n)]
        bit = [0] * (n+1)
        ans = 0
        for pos in coord:
            ans += self.get_sum(bit, n) - self.get_sum(bit, pos)
            self.update(bit, n, pos, 1)
        return ans

    def get_sum(self, bit, i):
        res = 0
        i += 1
        while i > 0:
            res += bit[i]
            i -= (i & -i)
        return res

    def update(self, bit, n, i, v):
        i += 1
        while i <= n:
            bit[i] += v
            i += (i & -i)
