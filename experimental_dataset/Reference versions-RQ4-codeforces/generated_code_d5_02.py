
def solve(heights):
    max_height = max(heights)
    winner_count = 0
    for height in heights:
        if height == max_height:
            winner_count += 1
            if winner_count > 1:
                return False
    return True


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
