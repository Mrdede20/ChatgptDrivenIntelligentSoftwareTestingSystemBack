First program:

```
import sys

class Solution:
    def BinaryInversions(self, n, bits):
        first = list(bits)
        second = list(bits)
        orig = list(bits)
        hasFirst = True
        hasSecond = True
        
        firstZero = -1
        lastOne = -1
        
        for i in range(n):
            if bits[i] == "0":
                if hasFirst:
                    first[i] = "1"
                    firstZero = i
                    hasFirst = False
                else:
                    second[i] = "1"
            else:
                if hasSecond:
                    second[i] = "0"
                    lastOne = i
                    hasSecond = False
                else:
                    first[i] = "0"
        
        firstZeros = 0
        secondZeros = 0
        origZeros = 0
        
        for i in range(n):
            if i < firstZero and first[i] == "0":
                firstZeros += 1
            if i < lastOne and second[i] == "0":
                secondZeros += 1
            if orig[i] == "0":
                origZeros += 1
                
        return max(firstZeros, secondZeros, origZeros)

n, bits = input().split()
n = int(n)
print(Solution().BinaryInversions(n, bits))
```

Second program (a slightly optimized version of the first program):

```
import sys

class Solution:
    def BinaryInversions(self, n, bits):
        first = list(bits)
        second = list(bits)
        hasFirst = True
        hasSecond = True
        
        firstZero = -1
        lastOne = -1
        
        for i in range(n):
            if bits[i] == "0":
                if hasFirst:
                    first[i] = "1"
                    firstZero = i
                    hasFirst = False
                else:
                    second[i] = "1"
            else:
                if hasSecond:
                    second[i] = "0"
                    lastOne = i
                    hasSecond = False
                else:
                    first[i] = "0"
        
        firstZeros = first[:firstZero].count("0")
        secondZeros = second[:lastOne].count("0")
        origZeros = bits.count("0") - orig[:firstZero+1].count("0") - orig[lastOne:].count("0")
                
        return max(firstZeros, secondZeros, origZeros)

n, bits = input().split()
n = int(n)
print(Solution().BinaryInversions(n, bits))
```