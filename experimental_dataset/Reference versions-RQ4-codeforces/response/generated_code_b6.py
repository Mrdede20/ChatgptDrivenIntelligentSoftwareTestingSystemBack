Certainly! Here are two example programs that achieve this intention: 

Example Program 1:

```python
def max_ascii_code(n: int) -> None:
    highest_ascii_code = 0
    
    for i in range(n):
        num, string = input().split()
        
        for char in string:
            ascii_code = ord(char)
            if ascii_code > highest_ascii_code:
                highest_ascii_code = ascii_code
                
    position_of_highest_letter = highest_ascii_code - 96
    print(position_of_highest_letter)
```

Example Program 2: 

```python
def max_ascii_code(n: int) -> None:
    highest_ascii_code = 0
    
    for i in range(n):
        num, string = input().split()
        ascii_list = [ord(char) for char in string]
        max_ascii_code_in_string = max(ascii_list)
        
        if max_ascii_code_in_string > highest_ascii_code:
            highest_ascii_code = max_ascii_code_in_string
                
    position_of_highest_letter = highest_ascii_code - 96
    print(position_of_highest_letter)
```

Both of these programs take an integer `n` as input, followed by `n` lines of input each containing a positive integer and a string. The program then finds the maximum ASCII code of the characters in each string and keeps track of the overall highest ASCII code. Finally, the program prints the difference between the highest ASCII code and 96, which is the position of the highest letter in the English alphabet.