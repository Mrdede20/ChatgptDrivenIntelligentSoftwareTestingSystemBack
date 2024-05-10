
class Solution:
    def BinaryInversions(self, n, bits):
        # calculate the number of inversions in the original bits
        count = self.countInversions(bits)

        # calculate the number of inversions when first 0 is inverted to 1
        count1 = count
        for i in range(n):
            if bits[i] == 0:
                count1 += 1
                break

        # calculate the number of inversions when last 1 is inverted to 0
        count2 = count
        for i in range(n - 1, -1, -1):
            if bits[i] == 1:
                count2 += 1
                break

        return max(count, count1, count2)

    def countInversions(self, bits):
        n = len(bits)
        count = 0
        ones = 0
        zeros = 0
        for i in range(n):
            if bits[i] == 1:
                count += zeros
                ones += 1
            else:
                count += ones
                zeros += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    while True:
        try:
            n = int(input())
            bits = list(map(int, input().split()))
            print(solution.BinaryInversions(n, bits))
        except EOFError:
            break
