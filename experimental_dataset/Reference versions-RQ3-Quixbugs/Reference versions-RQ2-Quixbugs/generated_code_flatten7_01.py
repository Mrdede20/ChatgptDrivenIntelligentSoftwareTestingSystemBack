
def flatten(input_list):
    for elem in input_list:
        if isinstance(elem, list):
            yield from flatten(elem)
        else:
            yield elem

# Example usage
input_list = [1, 2, [3, 4], 5, [6, [7, 8]]]
output_list = list(flatten(input_list))
print(output_list)
