
def next_palindrome(digits):
    length = len(digits)
    mid = length // 2
    left = mid - 1 if length % 2 == 0 else mid
    right = mid + 1 if length % 2 == 0 else mid
    
    while left >= 0 and right < length:
        if digits[left] > digits[right]:
            digits[right] = digits[left]
            break
        elif digits[left] < digits[right]:
            digits[mid] += 1
            digits[left:right] = [0] * (right - left)
            break
        left -= 1
        right += 1
    else:
        digits[mid] += 1
        digits[:mid], digits[mid+1:] = [0] * mid, [0] * mid
        
    return digits
