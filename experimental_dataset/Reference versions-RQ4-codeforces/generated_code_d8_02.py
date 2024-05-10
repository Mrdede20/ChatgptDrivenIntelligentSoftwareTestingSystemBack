
def jump_to_mountain_possible(heights):
    valleys = []
    current_height = heights[0]
    for i in range(1, len(heights)):
        if heights[i] < current_height:
            j = i
            while j < len(heights) and heights[j] < current_height:
                j += 1
            valleys.append(heights[i-1:j])
            current_height = heights[j-1]
        else:
            current_height = heights[i]
    if len(valleys) < 2:
        return "NO"
    first_valley = valleys[0]
    last_valley = valleys[-1]
    if first_valley[0] < last_valley[-1]:
        return "NO"
    for i, height in enumerate(first_valley[1:], start=1):
        if height > first_valley[i-1]:
            break
    else:
        return "NO"
    for i in range(len(last_valley)-2, -1, -1):
        if last_valley[i] > last_valley[i+1]:
            break
    else:
        return "NO"
    return "YES"
