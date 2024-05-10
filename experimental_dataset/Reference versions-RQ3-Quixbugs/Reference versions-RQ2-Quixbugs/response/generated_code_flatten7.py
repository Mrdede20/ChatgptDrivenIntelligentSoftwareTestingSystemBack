Sure, here are two programs that achieve the same intention:

Program 1:

```python
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
```

Program 2:

```python
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
```

Both programs have the same method name `flatten` and take in one parameter, an input list. The first program uses `yield` to return a Python generator object that produces the flattened output list on-the-fly, while the second program collects the flattened elements in a list before returning it.