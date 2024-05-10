Program 1:

```
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    else:
        pivot = arr[0]
        lower = [i for i in arr[1:] if i <= pivot]
        upper = [i for i in arr[1:] if i > pivot]

        if k < len(lower):
            return quickselect(lower, k)
        elif k == len(lower):
            return pivot
        else:
            return quickselect(upper, k - len(lower) - 1)
```

Program 2:

```
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    else:
        pivot = arr[0]
        lower = [i for i in arr[1:] if i <= pivot]
        upper = [i for i in arr[1:] if i > pivot]

        if k < len(lower):
            return quickselect(lower, k)
        elif k == len(lower):
            return pivot
        else:
            new_k = k - len(lower) - 1
            return quickselect(upper, new_k)
```

Both of these programs implement the Quickselect algorithm in Python. They take in an array (arr) and an integer k as input and return the kth-lowest element of arr (0-based index). They use the same method name and parameter type as specified in the instructions. The main difference between the two programs is how they calculate the new value of k in the recursive call for the upper subarray. Program 1 subtracts len(lower) + 1 from k, while Program 2 calculates a new variable new_k and passes that to the recursive call.