
def powerset(arr):
    def generate(idx, current):
        if idx == len(arr):
            return [current]
        else:
            return generate(idx+1, current) + generate(idx+1, current+[arr[idx]])
        
    return generate(0, [])
