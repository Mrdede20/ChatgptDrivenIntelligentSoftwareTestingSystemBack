
class Solution:
    def BinaryInversions(self, n: int, bits: List[int]) -> int:
        def count_inversions(bitlist):
            if not bitlist:
                return 0
            n = len(bitlist)
            zeros = [0]*n
            for i in range(n-2,-1,-1):
                zeros[i] = zeros[i+1] + (bitlist[i+1] == 0)
            inversions = 0
            for i in range(n-1):
                if bitlist[i] == 1:
                    inversions += zeros[i]
            return inversions

        first = bits[:]
        for i in range(n):
            if bits[i] == 0:
                first[i] = 1
                break

        second = bits[::-1]
        for i in range(n):
            if second[i] == 1:
                second[i] = 0
                break

        orig_inversions = count_inversions(bits)
        first_inversions = count_inversions(first)
        second_inversions = count_inversions(second[::-1])

        return max(orig_inversions, first_inversions, second_inversions)
