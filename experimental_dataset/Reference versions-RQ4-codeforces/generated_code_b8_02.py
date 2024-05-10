
def find_alpha_pos(n: int):
    for i in range(n):
        a = int(input())
        s = input()
        max_val = 0
        for char in s:
            val = ord(char)
            if val > max_val:
                max_val = val
        diff = max_val - 96
        print(diff)
