
def find_middle(t):
    for i in range(t):
        a, b, c = map(int, input().split())
        arr = [a, b, c]
        arr.sort()
        print(arr[1])
