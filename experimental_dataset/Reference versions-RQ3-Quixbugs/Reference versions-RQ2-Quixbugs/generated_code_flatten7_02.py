
def flatten(input_list):
    output_list = []
    for elem in input_list:
        if isinstance(elem, list):
            output_list.extend(flatten(elem))
        else:
            output_list.append(elem)
    return output_list

# Example usage
input_list = [1, 2, [3, 4], 5, [6, [7, 8]]]
output_list = flatten(input_list)
print(output_list)
