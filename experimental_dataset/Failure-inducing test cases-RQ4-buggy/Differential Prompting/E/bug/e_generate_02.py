class Solution:
    def BinaryInversions(self, n, bits):
        zeros = [i for i, b in enumerate(bits) if b == 0]
        ones = [i for i, b in enumerate(bits) if b == 1]
        inversions = []
        
        # Case 1: flip one zero bit
        if zeros:
            for i in zeros:
                inv = sum([i < j for j in ones])
                inv += sum([i > j for j in zeros if j != i])
                inversions.append(inv)
        
        # Case 2: flip two zero bits
        if len(zeros) > 1:
            for i in range(len(zeros)):
                for j in range(i+1, len(zeros)):
                    inv = sum([k < zeros[i] for k in ones])
                    inv += sum([zeros[i] < k < zeros[j] for k in zeros])
                    inv += sum([zeros[j] < k for k in ones])
                    inversions.append(inv)
        
        # Case 3: flip one one bit
        if ones:
            for i in ones:
                inv = sum([i > j for j in zeros])
                inv += sum([i < j for j in ones if j != i])
                inversions.append(inv)
        
        # Case 4: flip two one bits
        if len(ones) > 1:
            for i in range(len(ones)):
                for j in range(i+1, len(ones)):
                    inv = sum([k < ones[i] for k in zeros])
                    inv += sum([ones[i] < k < ones[j] for k in ones])
                    inv += sum([ones[j] < k for k in zeros])
                    inversions.append(inv)
        
        return max(inversions, default=0)

sol = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    bits = list(map(int, input().split()))
    print(sol.BinaryInversions(n, bits))
