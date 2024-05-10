
def find_peak(mountain_range):
    peaks = []
    for i in range(1, len(mountain_range)-1):
        if mountain_range[i] > mountain_range[i-1] and mountain_range[i] > mountain_range[i+1]:
            peaks.append(i)
    if len(peaks) == 1:
        left = mountain_range[:peaks[0]]
        right = mountain_range[peaks[0]+1:]
        return max(left) < mountain_range[peaks[0]] and max(right) < mountain_range[peaks[0]]
    return False
