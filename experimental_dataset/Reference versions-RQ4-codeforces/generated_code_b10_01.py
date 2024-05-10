
def calc_alphabetical_position(N: int, tests: List[Tuple[int, str]]) -> List[int]:
    result = []
    for i in range(N):
        highest_ascii = 0
        integer, test_str = tests[i]
        for char in test_str:
            if ord(char) > integer:
                integer = ord(char)
        result.append(integer - 96)
    return result
