
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
        inv1 = self.find_inversions(bits, bin1)
        bin2 = bits.copy()
        bin2[first_one], bin2[first_zero] = bin2[first_zero], bin2[first_one]
        inv2 = self.find_inversions(bits, bin2)
        return max(inv1, inv2)

    def find_inversions(self, arr1, arr2):
        n = len(arr1)
        index_dict = {}
        for i in range(n):
            index_dict[arr1[i]] = i
        arr2.sort()
        vis = [False] * n
        ans = 0
        for i in range(n):
            if vis[i] or index_dict[arr2[i]] == i:
                continue
            cycle_size = 0
            j = i
            while not vis[j]:
                vis[j] = True
                j = index_dict[arr2[j]]
                cycle_size += 1
            if cycle_size > 0:
                ans += (cycle_size - 1)
        return ans
