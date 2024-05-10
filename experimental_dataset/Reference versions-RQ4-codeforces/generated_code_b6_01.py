
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
