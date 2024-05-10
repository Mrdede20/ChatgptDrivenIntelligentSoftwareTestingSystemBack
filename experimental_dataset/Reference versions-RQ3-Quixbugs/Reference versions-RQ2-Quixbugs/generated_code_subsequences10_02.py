
def subsequences(a, b, k):
    def helper(start, k, current):
        if k == 0:
            result.append(list(current))
            return
        for i in range(start, b-k+2):
            current.append(i)
            helper(i+1, k-1, current)
            current.pop()
            
    result = []
    helper(a, k, [])
    return result
