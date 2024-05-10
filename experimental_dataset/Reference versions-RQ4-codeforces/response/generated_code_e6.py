Program 1:

```
class Solution:
    def BinaryInversions(n: int, bits: List[int]) -> int:
        def countOnes(bitList):
            ones = 0
            for bit in bitList:
                if bit == 1:
                    ones += 1
            return ones
        
        def countInversions(bitList):
            inversions = 0
            for i in range(len(bitList)):
                for j in range(i+1, len(bitList)):
                    if bitList[i] > bitList[j]:
                        inversions += 1
            return inversions
        
        first = bits.copy()
        second = bits.copy()
        orig = bits.copy()
        hasFirst = True
        hasSecond = True
        
        for i in range(n):
            if bits[i] == 0 and hasFirst:
                first[i] = 1
                hasFirst = False
            elif bits[i] == 1 and hasSecond:
                second[i] = 0
                hasSecond = False
        
        first_sum = countInversions(first)
        second_sum = countInversions(second)
        orig_sum = countInversions(orig)
        first_zeros = n - countOnes(first)
        second_zeros = n - countOnes(second)
        orig_zeros = n - countOnes(orig)
        
        if hasFirst and hasSecond:
            return orig_sum
        elif hasFirst:
            if first_zeros < second_zeros:
                return orig_sum + first_sum
            else:
                return orig_sum + second_sum
        elif hasSecond:
            if second_zeros < first_zeros:
                return orig_sum + second_sum
            else:
                return orig_sum + first_sum
        else:
            return max(orig_sum, first_sum + second_sum)
```

Program 2:

```
class Solution:
    def BinaryInversions(n: int, bits: List[int]) -> int:
        def countOnes(bitList):
            ones = 0
            for bit in bitList:
                if bit == 1:
                    ones += 1
            return ones
        
        def countInversions(bitList):
            inversions = 0
            for i in range(len(bitList)):
                for j in range(i+1, len(bitList)):
                    if bitList[i] > bitList[j]:
                        inversions += 1
            return inversions
        
        first = bits.copy()
        second = bits.copy()
        orig = bits.copy()
        hasFirst = True
        hasSecond = True
        
        for i in range(n):
            if bits[i] == 0 and hasFirst:
                first[i] = 1
                hasFirst = False
            elif bits[i] == 1 and hasSecond:
                second[i] = 0
                hasSecond = False
        
        first_sum = countInversions(first)
        second_sum = countInversions(second)
        orig_sum = countInversions(orig)
        first_zeros = n - countOnes(first)
        second_zeros = n - countOnes(second)
        orig_zeros = n - countOnes(orig)
        
        if hasFirst and hasSecond:
            return orig_sum
        elif hasFirst:
            if first_zeros < second_zeros:
                return orig_sum + first_sum
            else:
                return orig_sum + second_sum
        elif hasSecond:
            if second_zeros < first_zeros:
                return orig_sum + second_sum
            else:
                return orig_sum + first_sum
        else:
            return max(orig_sum, first_sum + second_sum)
```