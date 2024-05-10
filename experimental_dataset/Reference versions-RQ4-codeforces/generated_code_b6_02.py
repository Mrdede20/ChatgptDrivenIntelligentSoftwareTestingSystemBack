
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
