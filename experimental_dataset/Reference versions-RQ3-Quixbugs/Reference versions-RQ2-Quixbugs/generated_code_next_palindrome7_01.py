
def find_next_palindrome(digit_list):
    n = len(digit_list)
    left = n // 2 - 1
    right = (n+1) // 2
    middle = (left, right) if n % 2 != 0 else (left,)
    is_left_smaller = False
    while left >= 0 and digit_list[left] == digit_list[right]:
        left -= 1
        right += 1
    if left < 0 or digit_list[left] < digit_list[right]:
        is_left_smaller = True
    while middle:
        if is_left_smaller:
            digit_list[middle[0]] += 1
            if digit_list[middle[0]] == 10:
                digit_list[middle[0]] = 0
                is_left_smaller = True
            else:
                is_left_smaller = False
        for i in middle:
            digit_list[i] = digit_list[-i-1]
        middle = middle[:-1] if n % 2 == 0 else None
    if is_left_smaller:
        digit_list.insert(0, 1)
        digit_list[-1] = 1
    return digit_list
