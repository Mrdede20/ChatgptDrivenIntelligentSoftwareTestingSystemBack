Here are two versions of the program that achieves this intention:

Version 1:

```
def find_peak(mountain_range):
    peaks = []
    for i in range(1, len(mountain_range)-1):
        if mountain_range[i] > mountain_range[i-1] and mountain_range[i] > mountain_range[i+1]:
            peaks.append(i)
    if len(peaks) == 1:
        left = mountain_range[:peaks[0]]
        right = mountain_range[peaks[0]+1:]
        if max(left) < mountain_range[peaks[0]] and max(right) < mountain_range[peaks[0]]:
            return True
    return False
```

Version 2:

```
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
```

Both versions work by iterating over the list of integers using a for loop. At each index in the loop, the code checks if the integer at that index is greater than the integers to its left and right. If so, that index is added to a list of peaks.

If there is only one peak in the list, the code extracts the left and right sublists using slicing, then checks if the maximum value in each sublist is less than the peak's altitude. If so, the function returns True indicating that there is a single highest peak in the range. Otherwise, the function returns False.