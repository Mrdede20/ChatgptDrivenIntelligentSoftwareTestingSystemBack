
def find_next_palindrome(digit_list):
    n = len(digit_list)
    mid = n // 2
    left = mid - 1
    right = mid + 1 if n % 2 == 1 else mid
    while left >= 0 and digit_list[left] == digit_list[right]:
        left -= 1
        right += 1
    if left < 0 or digit_list[left] < digit_list[right]:
        left = mid - 1
        carry = 1
        if n % 2 == 1:
            digit_list[mid] += carry
            carry = digit_list[mid] // 10
            digit_list[mid] %= 10
            right = mid + 1
        else:
            right = mid
        while left >= 0:
            digit_list[left] += carry
            carry = digit_list[left] // 10
            digit_list[left] %= 10
            digit_list[right] = digit_list[left]
            left -= 1
            right += 1
        if carry > 0:
            digit_list.insert(0, carry)
            digit_list.append(carry)
    else:
        while left >= 0:
            digit_list[right] = digit_list[left]
            left -= 1
            right += 1
    return digit_list
