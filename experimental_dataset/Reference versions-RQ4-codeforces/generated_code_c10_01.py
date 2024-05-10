
def max_difference(t, n, s):
    for i in range(t):
        max1 = max2 = float('-inf')
        for num in s[i]:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        for num in s[i]:
            if num == max1:
                print(max1 - max2)
            else:
                print(max1 - num)
