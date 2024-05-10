
def find_middle(t):
    while t != 0:
        a, b, c = map(int, input().split())
        arr = [a, b, c]
        arr.sort()
        print(arr[1])
        t -= 1
