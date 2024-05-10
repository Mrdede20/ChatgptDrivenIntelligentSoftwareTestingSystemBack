
def next_palindrome(digits):
    n = len(digits)
    if n%2 == 0:
        mid = n//2 - 1
    else:
        mid = n//2
    left = mid
    right = mid + 1 if n%2 == 0 else mid
    while left >= 0 and right < n and digits[left] == digits[right]:
        left -= 1
        right += 1
    if left < 0 or digits[left] < digits[right]:
        digits[left+1:right] = digits[mid::-1]
    else:
        carry = 1
        i = mid
        while i >= 0:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            digits[n-1-i] = digits[i]
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
            digits[-1] = 1
    return digits
