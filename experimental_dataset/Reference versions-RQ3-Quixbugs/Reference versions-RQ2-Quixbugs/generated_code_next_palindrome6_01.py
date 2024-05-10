
def next_palindrome(digit_list):
    length = len(digit_list)
    mid = length // 2
    left = mid - 1
    right = mid + 1 if length % 2 else mid
    while left >= 0 and digit_list[left] == digit_list[right]:
        left -= 1
        right += 1
    if left < 0 or digit_list[left] < digit_list[right]:
        carry = 1
        mid = length // 2
        if length % 2 == 0:
            mid -= 1
        while mid >= 0 and carry > 0:
            digit_list[mid] += carry
            carry = digit_list[mid] // 10
            digit_list[mid] %= 10
            digit_list[length - mid - 1] = digit_list[mid]
            mid -= 1
        if carry > 0:
            digit_list.insert(0, carry)
            digit_list.append(carry)
    else:
        while left >= 0:
            digit_list[right] = digit_list[left]
            left -= 1
            right += 1
    return digit_list
