
class Solution:
    def BinaryInversions(self, n, bits):
        def count_inversions(arr):
            count = 0
            for i in range(len(arr)):
                for j in range(i+1,len(arr)):
                    if arr[i]>arr[j]:
                        count += 1
            return count
        def compute_sum(arr):
            sum_ = 0
            count_ = 0
            for val in arr[::-1]:
                if val == 1:
                    sum_ += count_
                elif val == 0:
                    count_ += 1
            return sum_
        
        first = bits[:]
        second = bits[:]
        orig = bits[:]
        hasFirst = True
        hasSecond = True
        
        for i in range(n):
            if hasFirst and bits[i] == 0:
                first[i] = 1
                hasFirst = False
            if hasSecond and bits[n-i-1] == 0:
                second[n-i-1] = 1
                hasSecond = False
                
        orig_sum = compute_sum(orig)
        first_sum = compute_sum(first)
        second_sum = compute_sum(second)
        
        return max(orig_sum,first_sum,second_sum)
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        bits = list(map(int,input().split()))
        sol = Solution()
        print(sol.BinaryInversions(n,bits))
