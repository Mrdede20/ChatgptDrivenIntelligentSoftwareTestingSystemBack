
def hanoi(height, start, end, middle):
    if height == 0:
        return []
    else:
        return (hanoi(height-1,start,middle,end) + 
               [(start,end)] + 
               hanoi(height-1,middle,end,start))
