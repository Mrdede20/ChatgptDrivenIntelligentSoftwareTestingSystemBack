t = int(input())   # Take input for the number of sets

while t > 0:   # Loop through each set of numbers
    numbers = input().split()   # Take input for a set of three integers and split them into a list
    numbers = [int(num) for num in numbers]   # Convert the input from string to integer
    
    numbers.sort()   # Sort the numbers in ascending order
    second_largest = numbers[1]   # Get the second largest number
    
    print(second_largest)   # Print the second largest number for the current set
    t -= 1   # Decrement t by 1
