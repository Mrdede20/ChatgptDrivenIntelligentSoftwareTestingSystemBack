# # Define a function to perform the transformation on a list
# def transform_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         max_val = max(lst)
#         second_max_val = max([x for x in lst if x != max_val])
#         return [x - max_val if x != max_val else x - second_max_val for x in lst]

# # Prompt the user for the number of test cases
# num_tests = int(input())

# # Loop through each test case
# for i in range(num_tests):
#     # Prompt the user for the number of integers and the list of integers
#     num_ints = int(input())
#     int_list = list(map(int, input().split()))

#     # Transform the list and print the result
#     result = transform_list(int_list)
#     print(*result)
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = list(map(int, input().split()))
#     sorted_s = sorted(s)
#     max_elem = max(s)
#     second_max_elem = sorted_s[-2] if n > 1 else max_elem
#     li = [elem - second_max_elem if elem == max_elem else elem - max_elem for elem in s]
#     print(*li)

t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the length of the array
    s = list(map(int, input().split()))  # Read the array of integers
    
    # Find the indices of the two maximum elements in the array
    mx1 = max(range(n), key=lambda i: s[i])
    mx2 = max([i for i in range(n) if i != mx1], key=lambda i: s[i])
    
    # Print the differences between each element and the two maximums
    for i in range(n):
        if i == mx1:
            print(s[i] - s[mx2], end=" ")
        else:
            print(s[i] - s[mx1], end=" ")
            
    print()  # Move to the next line for the next test case
