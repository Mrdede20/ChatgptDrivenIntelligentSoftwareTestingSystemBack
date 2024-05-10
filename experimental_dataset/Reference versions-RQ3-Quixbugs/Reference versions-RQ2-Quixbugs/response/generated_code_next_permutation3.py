Here are two Python programs that generate the next lexicographically greater permutation of a list of unique integers using the same function name and parameter type:

Program 1:
```python
def next_permutation(lst):
    i = len(lst) - 2
    while i >= 0 and lst[i] >= lst[i + 1]:
        i -= 1
    if i == -1:
        return lst[::-1]
    else:
        j = len(lst) - 1
        while lst[j] <= lst[i]:
            j -= 1
        lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1:] = lst[:i:-1]
        return lst
```

Program 2:
```python
def next_permutation(lst):
    i = len(lst) - 2
    while i >= 0 and lst[i] >= lst[i + 1]:
        i -= 1
    if i == -1:
        return lst[::-1]
    j = len(lst) - 1
    while lst[j] <= lst[i]:
        j -= 1
    lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1:] = lst[:i:-1]
    return lst
```

Both programs follow the same algorithm for generating the next lexicographically greater permutation of a list of unique integers. They start by checking if the input list is in reverse order. If it is, they simply return the list in reverse order, which is the lexicographically smallest permutation. Otherwise, they loop through the elements of the list from the second last element to the first element, looking for a decreasing sequence. If they find such a sequence, they swap the smallest element in the sequence with the next largest element in the list, and then reverse the sublist to the right of the swapped element. This generates the lexicographically next permutation of the list with the given permutation.