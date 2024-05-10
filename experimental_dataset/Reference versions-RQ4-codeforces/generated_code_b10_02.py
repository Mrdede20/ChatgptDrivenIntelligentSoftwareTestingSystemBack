
def calc_alphabetical_position(N: int, tests: List[Tuple[int, str]]) -> List[int]:
    result = []
    for i in range(N):
        integer, test_str = tests[i]
        highest_char_pos = max([ord(char) for char in test_str if ord(char) > integer]) - 96
        result.append(highest_char_pos)
    return result
