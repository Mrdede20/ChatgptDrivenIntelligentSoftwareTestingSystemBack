def binary_inversions(n, bits):
    # create copies of the bits list
    first = bits[:]
    second = bits[:]
    orig = bits[:]

    # find the first zero from the left and the first one from the right
    has_first = has_second = True
    for i in range(n):
        if has_first and bits[i] == 0:
            first[i] = 1
            has_first = False
        if has_second and bits[n-i-1] == 1:
            second[n-i-1] = 0
            has_second = False

    # compute the number of inversions for each list
    first_sum = second_sum = orig_sum = 0
    first_zeros = second_zeros = orig_zeros = 0
    for i in range(n-1, -1, -1):
        if first[i] == 0:
            orig_zeros += 1
        else:
            orig_sum += orig_zeros
        if second[i] == 0:
            second_zeros += 1
        else:
            second_sum += second_zeros

        if first[i] == 0:
            first_zeros += 1
        else:
            first_sum += first_zeros

    # return the maximum number of inversions
    return max(orig_sum, first_sum, second_sum)


t = int(input())
for _ in range(t):
    n = int(input())
    bits = list(map(int, input().split()))
    print(binary_inversions(n, bits))
