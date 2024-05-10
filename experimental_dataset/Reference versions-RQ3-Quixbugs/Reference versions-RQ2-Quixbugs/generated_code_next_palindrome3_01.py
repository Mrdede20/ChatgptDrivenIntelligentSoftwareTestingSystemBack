
def next_palindrome(digits):
    length = len(digits)
    mid = length // 2
    left = mid - 1 if length % 2 == 0 else mid
    right = mid + 1 if length % 2 == 0 else mid
    
    while left >= 0 and right < length:
        if digits[left] != digits[right]:
            if digits[left] > digits[right]:
                digits[right] = digits[left]
            else:
                carry = 1
                i = mid - 1 if length % 2 == 0 else mid
                while i >= 0 and carry == 1:
                    digits[i] += carry
                    carry = digits[i] // 10
                    digits[i] %= 10
                    digits[length - i - 1] = digits[i]
                    i -= 1
        left -= 1
        right += 1
    
    if carry == 1:
        digits = [1] + [0] * (length - 1) + [1]
        
    return digits
