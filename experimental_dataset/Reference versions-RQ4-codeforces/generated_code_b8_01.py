
def find_alpha_pos(n: int):
    for i in range(n):
        a = int(input())
        s = input()
        max_char = max(s)
        diff = ord(max_char) - 96
        print(diff)
