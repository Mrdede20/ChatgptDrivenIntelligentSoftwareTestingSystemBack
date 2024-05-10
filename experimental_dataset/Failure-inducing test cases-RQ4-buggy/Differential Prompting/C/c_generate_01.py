# # function to transform a given list of integers
# def transform_list(l):
#     n = len(l)
#     # if the list has only one element, return it
#     if n == 1:
#         return [l[0]]
#     # find the maximum and second maximum values in the list
#     maxx = max(l)
#     m2 = max([x for x in l if x < maxx])
#     # apply the transformation to the list
#     for i in range(n):
#         if l[i] == maxx:
#             l[i] -= m2
#         else:
#             l[i] -= maxx
#     return l

# # prompt the user to input the number of test cases
# num_tests = int(input())

# # loop through each test case
# for i in range(num_tests):
#     # prompt the user to input the number of integers in the list
#     num_ints = int(input())
#     # prompt the user to input the actual list of integers
#     int_list = list(map(int, input().split()))
#     # transform the list and print the result
#     result = transform_list(int_list)
#     print(*result)

# Function to compute differences between array elements and the maximum/second maximum element
# def compute_differences(n, s):
#     # Sort the array to find the maximum and second maximum elements
#     sorted_s = sorted(s)
#     max_val = sorted_s[-1]
#     second_max_val = sorted_s[-2]

#     # Initialize the list of differences
#     diff_list = []
#     for i in range(n):
#         if s[i] == max_val:
#             # If the element is equal to the maximum value, compute the difference with the second maximum value
#             diff_list.append(s[i] - second_max_val)
#         else:
#             # Otherwise, compute the difference with the maximum value
#             diff_list.append(s[i] - max_val)

#     return diff_list

# # Read the number of test cases
# t = int(input())

# # Iterate over each test case
# for _ in range(t):
#     # Read the size of the array and the array elements
#     n = int(input())
#     s = list(map(int, input().split()))

#     # Compute the differences and print the result
#     diff_list = compute_differences(n, s)
#     print(*diff_list)

# Define a function to process each test case
def process_test_case():
    # Read input values
    n = int(input())
    s = list(map(int, input().split()))
    
    # Find the indices of the two maximum elements
    mx = [0, 1] if s[0] > s[1] else [1, 0]
    for i in range(2, n):
        if s[i] > s[mx[0]]:
            mx[1] = mx[0]
            mx[0] = i
        elif s[i] > s[mx[1]]:
            mx[1] = i
    
    # Print the differences for each element in the array
    for i in range(n):
        if i == mx[0]:
            print(s[i] - s[mx[1]], end=' ')
        else:
            print(s[i] - s[mx[0]], end=' ')
    print()

# Read the number of test cases
t = int(input())

# Process each test case
for i in range(t):
    process_test_case()
