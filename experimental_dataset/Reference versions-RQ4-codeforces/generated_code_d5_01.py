
def solve(heights):
    max_height = max(heights)
    if heights.count(max_height) == 1:
        return True
    else:
        return False
     
     
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        heights = list(map(int, input().split()))
        result = solve(heights)
        if result:
            print("YES")
        else:
            print("NO")
