
def find_next_palindrome(digit_list):
    n = len(digit_list)
    mid = n//2
    left, right = mid-1, mid+1 if n%2 else mid
    
    while left >= 0 and digit_list[left] == digit_list[right]:
        left -= 1
        right += 1
        
    if left < 0 or digit_list[left] < digit_list[right]:
        carry = 1
        mid_val = digit_list[mid] + carry
        digit_list[mid] = mid_val % 10
        carry = mid_val // 10
        left, right = mid-1, mid+1 if n%2 else mid
        
        while carry > 0 and left >= 0:
            val = digit_list[left] + carry
            digit_list[left] = val % 10
            carry = val // 10
            digit_list[right] = digit_list[left]
            left -= 1
            right += 1
            
    else:
        left, right = mid-1, mid+1 if n%2 else mid
        
        while left >= 0:
            digit_list[right] = digit_list[left]
            left -= 1
            right += 1
            
    return digit_list
