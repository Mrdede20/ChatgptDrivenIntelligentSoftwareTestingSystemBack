
def generate_sequences(a, b, k):
    if k == 1:
        return [[i] for i in range(a, b+1)]
    
    result = []
    for i in range(a, b-k+2):
        sequences = generate_sequences(i+1, b, k-1)
        for sequence in sequences:
            result.append([i] + sequence)
    
    return result
